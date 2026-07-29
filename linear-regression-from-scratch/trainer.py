from loss import calculate_residuals
from loss import mean_squared_error


def train(model, X, y, learning_rate, epochs):

    n = len(X)

    for epoch in range(epochs):

        gradient_w = 0
        gradient_b = 0

        for x, actual in zip(X, y):

            prediction = model.predict(x)

            error = prediction - actual

            gradient_w += error * x
            gradient_b += error

        gradient_w = (2 / n) * gradient_w
        gradient_b = (2 / n) * gradient_b

        model.weight -= learning_rate * gradient_w
        model.bias -= learning_rate * gradient_b

        predictions = []

        for x in X:
            predictions.append(model.predict(x))

        residuals = calculate_residuals(y, predictions)

        loss = mean_squared_error(residuals)

        print(
            f"Epoch {epoch + 1:2d} | "
            f"Loss = {loss:.2f}"
        )

    return model