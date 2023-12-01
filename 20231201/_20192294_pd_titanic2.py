import pandas as pd
import numpy as np

titanic_df = pd.read_csv("titanic.csv")

print(titanic_df.groupby(["Sex"])[["Survived"]].sum())
