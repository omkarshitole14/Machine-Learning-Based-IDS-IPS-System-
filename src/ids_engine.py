import pickle
import pandas as pd

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_traffic(row):

    df = pd.DataFrame([row])

    prediction = model.predict(df)[0]

    return prediction