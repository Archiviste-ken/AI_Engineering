# 🔵 neuron.py

# This file upgrades the Lesson 2 neuron so it can work with Value objects.
# The logic stays the same: multiply each input by its weight, add everything
# together, then add a bias term.

import random  # 🎲 Use random initialization so the neuron starts with a unique guess.

from value import Value  # 🔌 Import the graph-aware scalar type used everywhere in Lesson 3.


class Neuron:  # 🧠 One neuron is the smallest trainable unit in this lesson.
    # It keeps a list of weights and one bias, both stored as Value objects.

    def __init__(self, n_inputs):  # 🏗️ Create as many weights as the neuron has inputs.
        # Each input gets its own learnable weight.
        self.weights = [
            Value(random.uniform(-1, 1))  # 🎯 Start from a random point in parameter space.
            for _ in range(n_inputs)  # 🔁 Repeat once for every incoming feature.
        ]

        # The bias lets the neuron shift its output without needing an input.
        self.bias = Value(random.uniform(-1, 1))  # 🎚️ Another trainable scalar, initialized randomly.

    def forward(self, inputs):  # 🚀 Compute the neuron's raw activation value.
        # The weighted sum begins at zero and accumulates contributions one by one.
        total = 0

        # Pair each weight with its matching input value and accumulate the score.
        for weight, input_value in zip(self.weights, inputs):  # 🤝 Match parameter to feature.
            total += weight * input_value  # ✖️ Multiply input influence by learned strength.

        # Add the bias at the end so the neuron can move its threshold freely.
        total += self.bias  # ➕ Final offset before returning the neuron's output.

        # Return the raw value; activation functions come later in the lesson.
        return total  # 📤 This output remains a Value so gradients can flow through it.