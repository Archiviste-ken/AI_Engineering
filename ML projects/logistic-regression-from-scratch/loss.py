
import math


def binary_cross_entropy(actual, prediction):

    epsilon = 1e-15
    prediction = max(
        epsilon,
        min(prediction, 1 - epsilon)
    )

    loss = -(
        actual * math.log(prediction)
        +
        (1 - actual) * math.log(1 - prediction)
    )

    return loss