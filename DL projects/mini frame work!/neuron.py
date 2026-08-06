import random

from value import Value


class Neuron:
    def __init__(self, n_inputs):
        self.weights = [Value(random.uniform(-1, 1)) for _ in range(n_inputs)]
        self.bias = Value(random.uniform(-1, 1))

    def forward(self, inputs):
        total = self.bias
        for weight, input_value in zip(self.weights, inputs):
            total += weight * input_value
        return total

    def parameters(self):
        return self.weights + [self.bias]