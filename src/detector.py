import pickle
import numpy as np

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


def predict_traffic(features):
    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]

    if prediction == 0:
        return "NORMAL"
    else:
        return "ANOMALY"