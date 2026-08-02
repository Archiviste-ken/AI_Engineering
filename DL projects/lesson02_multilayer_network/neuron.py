import random


class Neuron:

    def __init__(self, n_inputs):

        self.weights = [
            random.uniform(-1, 1)
            for _ in range(n_inputs)
        ]

        self.bias = random.uniform(-1, 1)

    def forward(self, inputs):

        total = 0

        for weight, input_value in zip(self.weights, inputs):
            total += weight * input_value

        total += self.bias

        return total