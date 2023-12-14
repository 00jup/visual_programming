import pandas as pd
import numpy as np

titanic_data = pd.read_csv("titanic.csv")

titanic_data = titanic_data.groupby(['Survived', 'Sex']).count()["PassengerId"]

Dead = 0
Survived = 1

print(
    f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[(Dead, "female")]+titanic_data.loc[(Survived, "female")]):.2%}')
print(
    f'{titanic_data.loc[(Dead, "male")]/(titanic_data.loc[(Dead, "male")]+titanic_data.loc[(Survived, "male")]):.2%}')
print(
    f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[(Dead)].sum()):.2%}')
print(
    f'{titanic_data.loc[(Dead, "female")]/(titanic_data.loc[:,"female"].sum()):.2%}')
