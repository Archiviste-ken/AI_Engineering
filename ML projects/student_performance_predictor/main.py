import pandas as pd

# Load dataset
data = pd.read_csv("data/student_performance.csv")

# Remove unnecessary columns
data = data.drop(columns=["student_id", "grade"])

# Features (Input)
X = data.drop(columns=["total_score"])

# Target (Output)
y = data["total_score"]

print("Features (X):")
print(X.head())

print("\nTarget (y):")
print(y.head())