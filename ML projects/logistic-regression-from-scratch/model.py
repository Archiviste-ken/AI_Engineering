import math


class LogisticRegression:

    def __init__(self):
        self.weight = 0.0
        self.bias = 0.0

    def sigmoid(self, z):
        return 1 / (1 + math.exp(-z))

    def predict(self, x):
        z = self.weight * x + self.bias
        return self.sigmoid(z)