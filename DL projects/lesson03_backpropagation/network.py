from layer import Layer


class Network:
    """
    🌐 A neural network is a sequence of layers.

    The output of one layer becomes the input
    to the next layer.
    """

    def __init__(self):

        self.layers = [
            Layer(2, 3),   # Hidden Layer
            Layer(3, 1)    # Output Layer
        ]

    def forward(self, inputs):

        for layer in self.layers:
            inputs = layer.forward(inputs)

        return inputs
    
    def parameters(self):
        """
        📦 Return every trainable parameter
        from every layer in the network.
        """

        params = []

        for layer in self.layers:
            params.extend(layer.parameters())

        return params
    
    def zero_grad(self):
        for parameter in self.parameters():
            parameter.grad = 0.0