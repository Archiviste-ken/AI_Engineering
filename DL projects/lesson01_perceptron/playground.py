from perceptron import Perceptron

xor_data = [
    ([0,0],0),
    ([0,1],1),
    ([1,0],1),
    ([1,1],0)
]
p = Perceptron(2)

print("Before Training")
print("----------------")
print("Weights:", p.weights)
print("Bias:", p.bias)

print("\nStarting Training...\n")

p.train(xor_data, epochs=100)


print("\nTraining Finished")
print("----------------")
print("Weights:", p.weights)
print("Bias:", p.bias)