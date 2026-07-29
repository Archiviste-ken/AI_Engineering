import matplotlib.pyplot as plt


def plot_regression(model, X, y):

    predictions = []

    for x in X:
        predictions.append(model.predict(x))

    plt.scatter(X, y, label="Actual Data")

    plt.plot(X, predictions, label="Regression Line")

    plt.xlabel("Study Hours")
    plt.ylabel("Marks")

    plt.title("Linear Regression From Scratch")

    plt.legend()

    plt.show()