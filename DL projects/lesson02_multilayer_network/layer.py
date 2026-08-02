# At the moment...

# This layer just stores neurons.

# It doesn't do anything yet.

from neuron import Neuron


class Layer:

    def __init__(self, n_inputs, n_neurons):

        self.neurons = []

        for _ in range(n_neurons):
            neuron = Neuron(n_inputs)
            self.neurons.append(neuron)
            
    def forward(self, inputs):

        outputs = []
        for neuron in self.neurons:
            output = neuron.forward(inputs)
            outputs.append(output)
        return outputs
