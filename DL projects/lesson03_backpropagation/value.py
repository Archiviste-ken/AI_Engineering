# 🟢 value.py ⭐⭐⭐⭐⭐

# This is the new file.

# It is the heart of Lesson 3.

# We'll build our own version of what PyTorch calls a Tensor (a simplified version).

# It will contain:

# ✅ Data
# ✅ Gradient
# ✅ Addition
# ✅ Multiplication
# ✅ Sigmoid
# ✅ Backward propagation
# ✅ Computational Graph

# This file is where most of Lesson 3 will happen.

class Value:

    def __init__(self, data, _children=(), _op=""):

        self.data = data

        self.grad = 0.0

        self._prev = set(_children)

        self._op = _op