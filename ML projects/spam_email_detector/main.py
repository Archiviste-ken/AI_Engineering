import pandas as pd
data = pd.read_csv("data/spam.csv", encoding="latin-1")

print(data.head())

print()

print(data.info())

print()

print(data.describe(include="all"))

# Remove empty columns
data = data.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"])

# Rename columns
data.columns = ["label", "message"]

print("\nAfter Cleaning:\n")
print(data.head())

print("\nColumns:")
print(data.columns)