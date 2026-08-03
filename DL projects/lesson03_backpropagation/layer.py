# 🟣 layer.py

# A layer is still just a small bundle of neurons.
# The structural idea is the same as Lesson 2; only the data type has changed.

from neuron import Neuron  # 🔌 Import the neuron building block used to populate the layer.


class Layer:  # 🧩 A layer groups several neurons that all see the same inputs.
    # It does not decide on its own; it only coordinates the neurons inside it.

    def __init__(self, n_inputs, n_neurons):  # 🏗️ Define the input width and neuron count.
        # Store the neurons in a simple list so we can iterate over them later.
        self.neurons = []

        # Create each neuron with the same input width.
        for _ in range(n_neurons):  # 🔁 Repeat for every neuron we want in this layer.
            neuron = Neuron(n_inputs)  # 🧠 Each neuron gets its own independent parameters.
            self.neurons.append(neuron)  # ➕ Collect the neuron into the layer.

    def forward(self, inputs):  # 🚀 Send one input vector through the full layer.
        # Gather each neuron's output here so we can pass the whole list onward.
        outputs = []

        # The print statement is part of the lesson's teaching trace.
        print("\nLayer Outputs:")  # 🖨️ Show the intermediate results clearly during the demo.

        # Every neuron receives the same input vector and produces one output.
        for neuron in self.neurons:  # 👀 Visit neurons one by one.
            output = neuron.forward(inputs)  # ⚙️ Ask one neuron to compute its response.
            outputs.append(output)  # 📥 Save the response in order.
            print(output)  # 🖨️ Display the neuron output for learning visibility.

        # The next layer will consume this list of Value objects.
        return outputs  # 📤 Return the full layer output as a list.
