from layer import Layer  # 🔌 Import Layer so the network can be built from stacked layers.


class Network:  # 🧠 Define the full neural network as an ordered set of layers.

    def __init__(self):  # 🏗️ Build the network architecture when a Network object is created.

        self.layers = []  # 📚 Keep all layers in one ordered list so data can flow through them.

        hidden_layer = Layer(  # 🌫️ Create the hidden layer, where the intermediate representation is formed.
            n_inputs=2,  # 📥 This layer expects two input values.
            n_neurons=3  # 🧮 This layer contains three neurons.
        )  # ✅ Finish creating the hidden layer.

        output_layer = Layer(  # 🎯 Create the output layer, which turns hidden features into the final result.
            n_inputs=3,  # 📥 This layer expects the three outputs from the hidden layer.
            n_neurons=1  # 🧾 This layer produces one final output value.
        )  # ✅ Finish creating the output layer.

        self.layers.append(hidden_layer)  # ➕ Add the hidden layer first so it receives the raw input.
        self.layers.append(output_layer)  # ➕ Add the output layer second so it receives the hidden layer output.
        
    def forward(self, inputs):  # 🚀 Run the complete forward pass through every layer in sequence.

        for layer in self.layers:  # 🔁 Move through the network one layer at a time.
            inputs = layer.forward(inputs) # 🔄 Replace the current inputs with the current layer's outputs.

        return inputs  # 📤 Return the final network output after the last layer finishes.