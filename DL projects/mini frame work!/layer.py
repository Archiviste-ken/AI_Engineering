from neuron import Neuron


class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.neurons = [Neuron(n_inputs) for _ in range(n_neurons)]

    def forward(self, inputs):
        return [neuron.forward(inputs) for neuron in self.neurons]

    def parameters(self):
        params = []
        for neuron in self.neurons:
            params.extend(neuron.parameters())
        return params