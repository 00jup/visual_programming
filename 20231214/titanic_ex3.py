import pandas as pd
import numpy as np

titanic_data = pd.read_csv("titanic.csv")

titanic_data["Age-band"] = np.floor(titanic_data[["Age"]]/10)*10
titanic_data = titanic_data["Age-band", "Survived", "PassengerId"].dropna()

titanic_data = titanic_data.astype({"Age-band": int})

titanic_data = titanic_data.groupby(
    ["Survived", "Age-band"]).count()["PassengerId"]

new_data = pd.DataFrame(index=[0, 10, 20, 30, 40, 50,
                               60, 70, 80], columns=["Survived People", "Dead People"])

new_data["Dead People"] = titanic_data.loc[0]
new_data["Survived People"] = titanic_data.loc[1]

new_data.to_csv("result.csv")