from perceptron import Perceptron

p = Perceptron(3)

p.weights = [2, -1, 3]
p.bias = -2

print(p.predict([1, 0, 1]))
print(p.predict([0, 1, 0]))
print(p.predict([1, 1, 1]))