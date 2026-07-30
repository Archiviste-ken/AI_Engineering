import pandas as pd
data = pd.read_csv("data/spam.csv", encoding="latin-1")
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)

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

# Convert labels into numbers
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})

print("\nAfter Label Encoding:\n")
print(data.head())

# Create Bag of Words
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(data["message"])

print("\nShape of Bag of Words Matrix:")
print(X.shape)

print("\nFirst 20 Words in Vocabulary:")
print(vectorizer.get_feature_names_out()[:20])

print("\nType of X:")
print(type(X))

print("\nFirst Message as a Dense Matrix:")
print(X[0].toarray())

# Create Features and Target
y = data["label"]

print("\nFeature Matrix Shape:")
print(X.shape)

print("\nTarget Shape:")
print(y.shape)

print("\nFirst 10 Labels:")
print(y.head(10))

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Feature Shape:", X_train.shape)
print("Testing Feature Shape :", X_test.shape)

print("\nTraining Labels Shape:", y_train.shape)
print("Testing Labels Shape :", y_test.shape)

# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(X_train, y_train)

print("\n✅ Logistic Regression Model Trained Successfully!")

# Predict classes
predictions = model.predict(X_test)

# Predict probabilities
probabilities = model.predict_proba(X_test)

print("\nFirst 10 Predictions:")
print(predictions[:10])

print("\nFirst 10 Probabilities:")
print(probabilities[:10])

print("\nFirst 10 Actual Labels:")
print(y_test.head(10))

# Model Evaluation
accuracy = accuracy_score(y_test, predictions)

print("\n📊 Model Accuracy")
print(f"Accuracy: {accuracy:.4f}")

print("\n📦 Confusion Matrix")
print(confusion_matrix(y_test, predictions))

print("\n📝 Classification Report")
print(classification_report(y_test, predictions))