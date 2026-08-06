def mse_loss(prediction, target):
    difference = prediction - target
    return difference * difference