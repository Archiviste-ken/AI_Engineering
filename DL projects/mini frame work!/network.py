from layer import Layer


class Network:
    def __init__(self):
        self.layers = [
            Layer(2, 3),
            Layer(3, 1),
        ]

    def forward(self, inputs):
        for layer in self.layers:
            inputs = layer.forward(inputs)
        return inputs

    def parameters(self):
        params = []
        for layer in self.layers:
            params.extend(layer.parameters())
        return params

    def zero_grad(self):
        for parameter in self.parameters():
            parameter.grad = 0.0