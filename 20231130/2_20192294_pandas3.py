import pandas as pd

titanic = pd.read_csv("titanic.csv")

print(titanic)

row = titanic.loc[1, :]
print(f"{row} \n")

# survived_people = titanic.loc[:, ["Survived"]]
survived_people = titanic.groupby("Sex")[["Survived"]].sum()

for column in survived_people:
    print(column)
    print(survived_people[column])
    print()

print(survived_people.head(1))
print(survived_people.tail(1))
