import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = pd.read_csv("data/Housing.csv")

print(data.head())
print("--------"*10)
print()
print("--------"*10)
print(data.info())
print("--------"*10)
print()
print(data.describe())

categorical_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus"
]

for column in categorical_columns:
    print(f"\n{column}:")
    print(data[column].unique())
    
binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for column in binary_columns:
    data[column] = data[column].map({
        "yes": 1,
        "no": 0
    })

print("\nAfter Binary Encoding:\n")
print(data.head())

data = pd.get_dummies(
    data,
    columns=["furnishingstatus"],
    dtype=int
)

print("\nAfter One-Hot Encoding:\n")
print(data.head())

X = data.drop(columns=["price"])
y = data["price"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

print("\nFeature Columns:")
print(X.columns)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Features:", X_train.shape)
print("Testing Features :", X_test.shape)

print("\nTraining Target :", y_train.shape)
print("Testing Target  :", y_test.shape)

model = LinearRegression()

model.fit(X_train, y_train)

print("\n✅ House Price Model Trained Successfully!")

predictions = model.predict(X_test)

print("\nPredicted Prices:")
print(predictions[:10])

print("\nActual Prices:")
print(y_test.head(10))

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n📊 Model Evaluation")
print(f"MAE : {mae:.2f}")
print(f"MSE : {mse:.2f}")
print(f"R²  : {r2:.4f}")