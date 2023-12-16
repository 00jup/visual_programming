import pandas as pd
import numpy as np

titanic_data = pd.read_csv("titanic.csv")

print(titanic_data["Survived"])
print()
print(titanic_data[["Survived"]])
titanic_data = titanic_data.groupby(
    ['Survived'])[['Sex', "PassengerId"]].sum()


# Dead = 0
# Survived = 1
# print(f"{titanic_data.loc[0].sum()}")
# print(f"{titanic_data.loc[1].sum()}")

# print(
#     f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[(Dead, "female")]+titanic_data.loc[(Survived, "female")]):.2%}')
# print(
#     f'{titanic_data.loc[(Dead, "male")]/(titanic_data.loc[(Dead, "male")]+titanic_data.loc[(Survived, "male")]):.2%}')
# print(
#     f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[(Dead)].sum()):.2%}')
# print(
#     f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[:,"female"].sum()):.2%}')
