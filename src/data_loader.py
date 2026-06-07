import pandas as pd
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder

def load_dataset(file_path, encoders=None):

    data, meta = arff.loadarff(file_path)

    df = pd.DataFrame(data)

    for col in df.columns:

        if df[col].dtype == object:

            df[col] = df[col].apply(
                lambda x: x.decode("utf-8")
                if isinstance(x, bytes)
                else x
            )

    if encoders is None:
        encoders = {}

        for col in df.select_dtypes(
            include=["object"]
        ).columns:

            le = LabelEncoder()

            df[col] = le.fit_transform(
                df[col].astype(str)
            )

            encoders[col] = le

    else:

        for col in encoders:

            df[col] = encoders[col].transform(
                df[col].astype(str)
            )

    return df, encoders