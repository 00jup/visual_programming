import pandas as pd

filename = "titanic.csv"
read_csv = pd.read_csv(filename)

read_csv = read_csv.groupby(["Survived", "Sex"]).count()["PassengerId"]

Dead = 0
Alive = 1
print(read_csv.size)
print(
    f"남자 사망자 대비 여자 사망자 \
        {read_csv.loc[(Dead, 'female')]/read_csv.loc[(Dead, 'male')]:.2%}")
print(
    f"남자 생존자 대비 여자 생존자 \
        {read_csv.loc[(Alive, 'female')]/read_csv.loc[(Alive, 'male')]:.2%}")
