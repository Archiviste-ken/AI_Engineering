# 🔵 neuron.py

# This file upgrades the Lesson 2 neuron so it can work with Value objects.
# The logic stays the same:
# Multiply each input by its weight, add everything together,
# then add a bias term.

import random

from value import Value


class Neuron:
    """
    🧠 A single neuron.

    It stores:
    - A weight for every input
    - One bias

    All parameters are Value objects so they can participate
    in the computational graph and receive gradients.
    """

    def __init__(self, n_inputs):
        
        """
        🏗️ Create the neuron.

        Every input gets its own random weight.
        The neuron also gets one random bias.
        """

        self.weights = [
            Value(random.uniform(-1, 1))
            for _ in range(n_inputs)
        ]

        self.bias = Value(random.uniform(-1, 1))

    def forward(self, inputs):
        """
        🚀 Compute the neuron's output.

        Formula:

        output = (w1*x1 + w2*x2 + ... + wn*xn) + bias

        Because weights and bias are Value objects,
        every multiplication and addition automatically
        builds the computational graph.
        """

        total = self.bias

        for weight, input_value in zip(self.weights, inputs):
            total += weight * input_value

        return total
    
    def parameters(self):
        return self.weights + [self.bias]