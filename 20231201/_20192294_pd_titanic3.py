import pandas as pd
import numpy as np

titanic_df = pd.read_csv("titanic.csv")

# print(titanic_df.groupby(["Age"])[["Sex"]])### 출력이 안 되는 이유?

titanic_df4 = titanic_df.groupby(["Sex"])[["Survived"]].sum()
titanic_df1 = titanic_df["Age"].dropna()
titanic_df2 = titanic_df[["Age", "Sex"]].dropna()
titanic_df3 = titanic_df[["Age"]][["Sex"]].dropna()


print(titanic_df1)
print(titanic_df2)
print(titanic_df4)


def age_cal(age):
    return age//10

# df["age_type"].apply(age_cal("Age"))


titanic_df["Age-Range"] = np.floor(titanic_df["Age"]/10)*10
