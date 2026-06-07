from src.data_loader import load_dataset

df, encoders = load_dataset("data/idsipsKDDTrain+.arff")

print(df.head())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)