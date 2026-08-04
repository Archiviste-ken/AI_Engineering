from network import Network
from loss import mse_loss

network = Network()

inputs = [1, 0]
target = 1

prediction = network.forward(inputs)

loss = mse_loss(prediction[0], target)

network.zero_grad()

loss.backward()

learning_rate = 0.1

for parameter in network.parameters():
    parameter.data -= learning_rate * parameter.grad