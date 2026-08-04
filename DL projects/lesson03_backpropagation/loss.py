from value import Value


def mse_loss(prediction, target):
    """
    📏 Mean Squared Error (MSE)

    Measures how far the prediction is
    from the target value.
    """

    difference = prediction - target
    return difference * difference