import pandas as pd
import numpy as np

titanic_df = pd.read_csv("titanic.csv")

# print(titanic_df.groupby(["Age"])[["Sex"]])### 출력이 안 되는 이유?

df = titanic_df["Age"].dropna()


def age_cal(age):
    return age//10

df["age_type"].apply(age_cal("Age"))