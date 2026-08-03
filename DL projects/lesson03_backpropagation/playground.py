# 🟡 playground.py

# Our testing laboratory 🧪.

# We'll use it to

# test Value
# test gradients
# visualize the computational graph
# test neurons
# test layers
# train the network
# train XOR

# This file will grow throughout the lesson.


from value import Value


# -------------------------------
# Create Values
# -------------------------------

a = Value(2.0)
b = Value(3.0)

print("Initial Values")
print("----------------")
print("a =", a.data)
print("b =", b.data)
print()


# -------------------------------
# Forward Pass
# -------------------------------

c = a * b          # 2 * 3 = 6
d = c + a          # 6 + 2 = 8

print("Forward Pass")
print("------------")
print("c = a * b =", c.data)
print("d = c + a =", d.data)
print()


# -------------------------------
# Graph Information
# -------------------------------

print("Graph Information")
print("-----------------")
print("c operation :", c._op)
print("d operation :", d._op)

print("c parents   :", [node.data for node in c._prev])
print("d parents   :", [node.data for node in d._prev])
print()


# -------------------------------
# Backward Pass
# -------------------------------

print("Running Backward...")
print("-------------------")

d.backward()

print("Gradients")
print("---------")
print("a.grad =", a.grad)
print("b.grad =", b.grad)
print("c.grad =", c.grad)
print("d.grad =", d.grad)