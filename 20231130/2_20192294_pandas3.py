import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv("titanic.csv")


# survived_people = titanic.loc[:, ["Survived"]]
survived_people = titanic[["Sex", "Survived", "PassengerId"]].dropna()
print(survived_people)

survived_people = survived_people.groupby(["Sex", "Survived"]).count()

print(survived_people)
survived_people.plot.bar()

plt.show()
