import pandas as pd

movies = pd.read_csv(r"C:\Users\irine\Downloads\archive (3)\movies.csv")
print(movies.head())
print("\nDataset shape:")
print(movies.shape)
print("\nColumns name:")
print(movies.columns)