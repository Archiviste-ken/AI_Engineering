# 🔴 network.py

# The network is still a stack of layers.
# The only real change is that every value moving through the stack is now a
# Value object, so the computation graph can record the whole path.

from layer import Layer  # 🔌 Import the layer abstraction used to build the stack.


class Network:  # 🧠 A Network is the full model made from multiple layers.
    # For this lesson the architecture is fixed and intentionally simple.

    def __init__(self):  # 🏗️ Assemble the network when the object is created.
        # Keep the layers in order so forward propagation is easy to follow.
        self.layers = []

        # The hidden layer transforms the raw 2D input into 3 learned features.
        hidden_layer = Layer(  # 🌫️ Learn an intermediate representation.
            n_inputs=2,  # 📥 The dataset examples have two input features.
            n_neurons=3,  # 🧮 Use three neurons to create a small hidden space.
        )

        # The output layer turns those three learned features into one final value.
        output_layer = Layer(  # 🎯 Produce the network's prediction.
            n_inputs=3,  # 📥 It receives the three hidden-layer outputs.
            n_neurons=1,  # 🧾 One output is enough for this lesson's toy problem.
        )

        # Append in execution order so the forward pass is just a simple loop.
        self.layers.append(hidden_layer)  # ➕ First transform the raw input.
        self.layers.append(output_layer)  # ➕ Then compress the hidden features.

    def forward(self, inputs):  # 🚀 Run the input through every layer in sequence.
        # Print the starting point so the demo is easier to read step by step.
        print(f"Original Input: {inputs}")

        # Each layer receives the previous layer's output.
        for layer in self.layers:  # 🔁 Walk through the model from left to right.
            print("-" * 40)  # 🧱 Visual separator for the lesson trace.
            print(f"Passing through Layer...")  # 🧭 Announce which stage we are in.
            inputs = layer.forward(inputs)  # 🔄 Replace current inputs with layer outputs.
            print(f"Hidden State: {inputs}")  # 👀 Show the new representation after the layer.

        # Final separator and result so the trace ends cleanly.
        print("-" * 40)  # 🧱 Closing divider for the network demo.
        print(f"Final Output: {inputs}")  # 🎯 Display the prediction-like output.

        # Return the last layer's output to the caller.
        return inputs  # 📤 The network output remains a list of Value objects.