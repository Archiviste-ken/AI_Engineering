from neuron import Neuron

class Layer:
    """
    🧠 A layer is just a collection of neurons.

    It forwards the same input to every neuron
    and collects all their outputs.
    """

    def __init__(self, n_inputs, n_neurons):

        self.neurons = [
            Neuron(n_inputs)
            for _ in range(n_neurons)
        ]

    def forward(self, inputs):

        outputs = [
            neuron.forward(inputs)
            for neuron in self.neurons
        ]

        return outputs
    
    def parameters(self):
        """
        📦 Return every trainable parameter
        from every neuron in this layer.
        """

        params = []

        for neuron in self.neurons:
            params.extend(neuron.parameters())

        return params
    