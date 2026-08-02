from neuron import Neuron


class Layer:

    def __init__(self, n_inputs, n_neurons):

        self.neurons = []

        for _ in range(n_neurons):
            neuron = Neuron(n_inputs)
            self.neurons.append(neuron)