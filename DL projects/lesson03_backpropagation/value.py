# 🟢 value.py ⭐⭐⭐⭐⭐

# This file is the engine of Lesson 3.
# It stores a number, remembers how it was created, and knows how gradients
# should flow backward through the tiny computational graph.


class Value:
    # A Value is a single scalar that can participate in a computation graph.

    def __init__(self, data, _children=(), _op=""):
        # The actual numeric payload carried by this node.
        self.data = data

        # The derivative of the final output with respect to this node.
        self.grad = 0.0

        # Keep references to the parents that produced this node.
        self._prev = set(_children)

        # Store the operation symbol so we can inspect the graph later.
        self._op = _op

        # Default backward hook does nothing until an operation replaces it.
        self._backward = lambda: None

    def __add__(self, other):
        """
        ➕ Add another Value or a Python number.
        """

        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad

        out._backward = _backward

        return out

    def __mul__(self, other):
        # Create a new node that represents the product of two Value objects.
        out = Value(
            self.data * other.data,
            (self, other),
            "*",
        )

        # Multiplication needs the product rule:
        # d(x * y)/dx = y and d(x * y)/dy = x.
        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        # Store that local derivative rule on the result node itself.
        out._backward = _backward

        # Return the product node so it can continue through the graph.
        return out
    
    def __repr__(self):
        """
        🖨️ Return a readable string representation
        of the Value object.
        """
        return f"Value(data={self.data}, grad={self.grad})"
    
    def __radd__(self, other):
        return self + other
    
    def __neg__(self):
        """
        ➖ Return the negative of this Value.

        -a is the same as (-1) * a.
        """
        return self * -1
    
    def __sub__(self, other):
        """
        ➖ Subtract another value.

        a - b = a + (-b)
        """
        return self + (-other)
    
    def __mul__(self, other):
        """
        ✖️ Multiply by another Value or Python number.
        """

        if not isinstance(other, Value):
            other = Value(other)

        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad

        out._backward = _backward

        return out
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        """
        ➗ Divide by another Value or Python number.

        a / b = a * (b ** -1)
        """

        if not isinstance(other, Value):
            other = Value(other)

        return self * (other ** -1)
    
    def __pow__(self, exponent):
        """
        🔼 Raise this Value to a numeric power.
        """

        assert isinstance(exponent, (int, float))

        out = Value(
            self.data ** exponent,
            (self,),
            f"**{exponent}"
        )

        def _backward():
            self.grad += (
                exponent
                * (self.data ** (exponent - 1))
                * out.grad
            )

        out._backward = _backward

        return out
    
    def backward(self):
        # Build the graph in topological order so parents are visited before
        # children during the reverse pass.
        topo = []
        visited = set()

        def build_topo(v):
            # Skip nodes we have already seen to avoid revisiting shared paths.
            if v not in visited:
                visited.add(v)

                # Recurse into every parent first.
                for child in v._prev:
                    build_topo(child)

                # Append the node only after all of its parents are processed.
                topo.append(v)

        # Start the traversal from the output node itself.
        build_topo(self)

        # The derivative of the output with respect to itself is 1.
        self.grad = 1.0

        # Walk backward through the graph and apply each node's local rule.
        for node in reversed(topo):
            node._backward()