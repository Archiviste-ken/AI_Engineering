class Perceptron:

    def __init__(self, n_inputs):
        self.weights = [0.0] * n_inputs
        self.bias = 0.0
        
    def predict(self, inputs):

     total = 0

     for weight, input_value in zip(self.weights, inputs):
        total += weight * input_value

     total += self.bias

     if total >= 0:
        return 1
     else:
        return 0