from network import Network
from loss import mse_loss

# 🧠 Create one network
network = Network()

# 📚 One training example
training_data = [
    ([0, 0], 0),
    ([0, 1], 1),
    ([1, 0], 1),
    ([1, 1], 0),
]

learning_rate = 0.1
epochs = 10000

for epoch in range(epochs):

    total_loss = 0

    for inputs, target in training_data:

        prediction = network.forward(inputs)

        loss = mse_loss(prediction[0], target)

        network.zero_grad()

        loss.backward()

        for parameter in network.parameters():
            parameter.data -= learning_rate * parameter.grad

        total_loss += loss.data

    print(
        f"Epoch {epoch + 1} | Loss = {total_loss:.4f}"
    )

print("\nFinal Predictions")
print("------------------")

for inputs, target in training_data:

    prediction = network.forward(inputs)

    print(
        f"Input: {inputs}"
        f" | Prediction: {prediction[0].data:.4f}"
        f" | Target: {target}"
    )