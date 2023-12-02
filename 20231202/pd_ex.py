import pandas as pd

titanic_df = pd.read_csv("titanic.csv")

print(titanic_df["Sex"])
print(titanic_df[["Sex"]])
