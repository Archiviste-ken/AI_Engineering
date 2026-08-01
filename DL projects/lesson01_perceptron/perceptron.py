class Perceptron:

    def __init__(self, n_inputs, learning_rate=0.1):
        self.weights = [0.0] * n_inputs
        self.bias = 0.0
        self.lr = learning_rate

    def predict(self, inputs):

        total = 0

        for weight, input_value in zip(self.weights, inputs):
            total += weight * input_value

        total += self.bias

        if total >= 0:
            return 1
        else:
            return 0

    def train(self, training_data, epochs):

     for epoch in range(epochs):
        errors = 0

        for inputs, target in training_data:

            prediction = self.predict(inputs)

            print("=" * 40)
            print(f"Epoch: {epoch + 1}")
            print(f"Inputs: {inputs}")
            print(f"Prediction: {prediction}")
            print(f"Target: {target}")

            error = target - prediction
            
            if error != 0:
                errors += 1

                print(f"Error: {error}")
                print(f"Old Weights: {self.weights}")
                print(f"Old Bias: {self.bias}")

                for i in range(len(self.weights)):
                    self.weights[i] += self.lr * error * inputs[i]

                self.bias += self.lr * error

                print(f"New Weights: {self.weights}")
                print(f"New Bias: {self.bias}")
        if errors == 0:
            
            print(f"Converged at epoch {epoch + 1}")
            return
        
     print(f"Did not converge after {epochs} epochs")