# 🔵 neuron.py

# We'll rewrite the neuron.

# Instead of using normal numbers like

# 0.5

# it will now use

# Value(0.5)

# Every weight and bias will become a Value object.

# Why?

# Because every number now needs to remember

# where it came from
# how it was computed
# how gradients flow through it

import random  # 🎲 Bring in Python's random number generator so the neuron can start with random values.
from value import Value

class Neuron:  # 🧠 Define one artificial neuron, the smallest computing unit in this lesson.

    def __init__(self, n_inputs):  # 🏗️ Build a neuron and tell it how many input values it should expect.

        self.weights = [  # ⚖️ Create one weight for each input so every input can have its own influence.
           Value(random.uniform(-1, 1))  # 🎯 Pick a random starting weight between -1 and 1.
            for _ in range(n_inputs)  # 🔁 Repeat that random choice once per input position.
        ]  # ✅ Finish the full list of initial weights.

        self.bias = Value(random.uniform(-1, 1))  # 🎚️ Give the neuron one extra adjustable offset that shifts the output.

    def forward(self, inputs):  # 🚀 Compute the neuron's output from the provided inputs.

        total = 0  # 🧮 Start the running sum at zero before combining weights and inputs.

        for weight, input_value in zip(self.weights, inputs):  # 🤝 Pair each weight with the matching input value.
            total += weight * input_value  # ✖️ Multiply the pair and add it into the accumulated score.

        total += self.bias  # ➕ Add the bias so the neuron can shift its decision threshold.

        return total  # 📤 Return the raw weighted sum, which is the neuron's output for this lesson.