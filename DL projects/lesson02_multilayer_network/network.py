from layer import Layer


class Network:

    def __init__(self):

        self.layers = []

        hidden_layer = Layer(
            n_inputs=2,
            n_neurons=3
        )

        output_layer = Layer(
            n_inputs=3,
            n_neurons=1
        )

        self.layers.append(hidden_layer)
        self.layers.append(output_layer)