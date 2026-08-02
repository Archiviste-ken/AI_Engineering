import random


class Neuron:

    def __init__(self, n_inputs):

        self.weights = [
            random.uniform(-1, 1)
            for _ in range(n_inputs)
        ]

        self.bias = random.uniform(-1, 1)