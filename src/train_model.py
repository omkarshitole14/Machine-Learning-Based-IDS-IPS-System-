import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from data_loader import load_dataset

# Load train data
train_df, encoders = load_dataset("data/idsipsKDDTrain+.arff")

X_train = train_df.drop("class", axis=1)
y_train = train_df["class"]

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    class_weight="balanced",
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# Save model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/encoders.pkl", "wb") as f:
    pickle.dump(encoders, f)

print("Model trained and saved successfully.")