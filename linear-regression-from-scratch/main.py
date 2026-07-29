from dataset import X, y
from model import LinearRegression
from loss import calculate_residuals, mean_squared_error
from trainer import train
from plot import plot_regression

model = LinearRegression()

predictions = []

for x in X:
    predictions.append(model.predict(x))

residuals = calculate_residuals(y, predictions)

mse = mean_squared_error(residuals)

print("Predictions:", predictions)
print("Residuals :", residuals)
print("MSE :", mse)

print("\nBefore Training")
print("Weight:", model.weight)
print("Bias:", model.bias)

model = train(
    model,
    X,
    y,
    learning_rate=0.01,
    epochs=1000
)

print("\nAfter Training")
print("Weight:", model.weight)
print("Bias:", model.bias)

print("\nFinal Predictions")
print("-" * 40)
print(f"{'Hours':<10}{'Actual':<10}{'Predicted'}")

for x, actual in zip(X, y):

    prediction = model.predict(x)

    print(f"{x:<10}{actual:<10}{prediction:.2f}")
    
print("\nLearned Equation")
print(f"Marks = {model.weight:.2f} × Hours + {model.bias:.2f}")

plot_regression(model, X, y)