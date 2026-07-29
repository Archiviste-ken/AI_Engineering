def calculate_residuals(actual, predicted):
    residuals = []

    for y_true, y_pred in zip(actual, predicted):
        residual = y_true - y_pred
        residuals.append(residual)

    return residuals

def mean_squared_error(residuals):

    squared_errors = []

    for r in residuals:
        squared_errors.append(r ** 2)

    mse = sum(squared_errors) / len(squared_errors)

    return mse