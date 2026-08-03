# 🟡 playground.py

# This is the tiny laboratory script for the lesson.
# It proves the Value class works before the network gets more complicated.

from value import Value  # 🔌 Import the graph-aware scalar type to test it directly.


# -------------------------------
# Create Values
# -------------------------------

# Start with two simple scalar nodes so the graph stays easy to inspect.
a = Value(2.0)  # 🧪 First test value.
b = Value(3.0)  # 🧪 Second test value.

print("Initial Values")  # 🖨️ Label the first section of the demo output.
print("----------------")  # 🧱 Visual divider so the notebook-style trace is easy to scan.
print("a =", a.data)  # 📌 Show the raw numeric payload for a.
print("b =", b.data)  # 📌 Show the raw numeric payload for b.
print()  # ↩️ Blank line for readability.


# -------------------------------
# Forward Pass
# -------------------------------

# Build a tiny graph: multiply first, then add.
c = a * b  # ✖️ This should create a node representing 2 * 3.
d = c + a  # ➕ This should create a node representing 6 + 2.

print("Forward Pass")  # 🖨️ Title for the forward-computation section.
print("------------")  # 🧱 Another divider so the output stays organized.
print("c = a * b =", c.data)  # 📌 Show the result of multiplication.
print("d = c + a =", d.data)  # 📌 Show the result of the addition.
print()  # ↩️ Space before the graph introspection section.


# -------------------------------
# Graph Information
# -------------------------------

# Inspect the metadata that proves the graph is being tracked.
print("Graph Information")  # 🖨️ Heading for the graph details.
print("-----------------")  # 🧱 Divider for the inspection block.
print("c operation :", c._op)  # 🧩 The stored operation that created c.
print("d operation :", d._op)  # 🧩 The stored operation that created d.

# Show each node's parents so the backward path is visible.
print("c parents   :", [node.data for node in c._prev])  # 🔎 Parents of multiplication.
print("d parents   :", [node.data for node in d._prev])  # 🔎 Parents of addition.
print()  # ↩️ Separate graph metadata from gradient results.


# -------------------------------
# Backward Pass
# -------------------------------

# Trigger reverse-mode autodiff from the final output node.
print("Running Backward...")  # 🖨️ Announce the gradient computation.
print("-------------------")  # 🧱 Divider so the trace is easy to read.

d.backward()  # 🔁 Propagate gradients from d back to a and b.

# Print the resulting gradients so we can verify the chain rule by hand.
print("Gradients")  # 🖨️ Label for the final section.
print("---------")  # 🧱 Divider for the gradient readout.
print("a.grad =", a.grad)  # 📈 Gradient flowing into a.
print("b.grad =", b.grad)  # 📈 Gradient flowing into b.
print("c.grad =", c.grad)  # 📈 Gradient flowing into c.
print("d.grad =", d.grad)  # 📈 Gradient of the output with respect to itself.