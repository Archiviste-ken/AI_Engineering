from network import Network

network = Network()

inputs = [1, 0]

prediction = network.forward(inputs)

print(prediction)