# 📝 At this stage, the layer is only a container for neurons.

# 🧱 It does not add activation, learning, or other logic yet.

from neuron import Neuron  # 🔌 Import the Neuron class so we can build layers out of neurons.


class Layer:  # 🧩 Define a layer, which is just a collection of neurons working together.

    def __init__(self, n_inputs, n_neurons):  # 🏗️ Create a layer with a fixed input size and a fixed neuron count.

        self.neurons = []  # 📦 Start with an empty list that will hold every neuron in this layer.

        for _ in range(n_neurons):  # 🔁 Repeat once for every neuron we want in the layer.
            neuron = Neuron(n_inputs)  # 🧠 Build one neuron that expects the same number of inputs.
            self.neurons.append(neuron)  # ➕ Store that neuron inside the layer.
            
    def forward(self, inputs):  # 🚀 Send one input vector through every neuron in the layer.

        outputs = []  # 🧺 Prepare a list to collect each neuron's output.
        print("\nLayer Outputs:")
        for neuron in self.neurons:  # 👀 Visit every neuron one by one.
            output = neuron.forward(inputs)  # ⚙️ Ask the neuron to compute its raw output from the same inputs.
            outputs.append(output) # 📥 Save that neuron's output in order.
            print(output)
        return outputs  # 📤 Return the full layer output as a list of neuron outputs.
