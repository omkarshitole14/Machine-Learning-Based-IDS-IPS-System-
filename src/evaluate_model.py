import pickle

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

from data_loader import load_dataset

# Load test data
with open(
    "models/encoders.pkl",
    "rb"
) as f:

    encoders = pickle.load(f)

test_df, _ = load_dataset(
    "data/idsipsKDDTest+.arff",
    encoders
)
X_test = test_df.drop("class", axis=1)
y_test = test_df["class"]

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

y_pred = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))