import numpy as np
import pandas as pd

filename = "titanic.csv"
data = pd.read_csv(filename)

data["Age-band"] = np.floor(data["Age"]/10)*10


data = data[["Age-band", "Fare", "Survived"]].dropna()
data = data.astype({"Age-band": int})

data = data.groupby(["Survived", "Age-band"]).mean()
# 순서 맞춰서 적는 습관가지기

# version1
new_data = pd.DataFrame(index=[0, 10, 20, 30, 40, 50, 60, 70, 80],
                        columns=["Dead", "Survived"])

new_data['Dead'] = data.loc[0]
new_data['Survived'] = data.loc[1]


new_data.to_csv("result.csv")

read = pd.read_csv("result.csv")

print(read)
