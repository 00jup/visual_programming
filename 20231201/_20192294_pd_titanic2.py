import pandas as pd
import numpy as np

titanic_df = pd.read_csv("titanic.csv")

# Version 1

# stat = titanic_df.groupby(['Survived', "Sex"]).count()['PassengerId'].values

# print(f'사망자 여성 비율: {stat[0]/(stat[0]+stat[1]):.2%}')
# print(f'사망자 남성 비율: {stat[1]/(stat[0]+stat[1]):.2%}')
# print(f'생존자 여성 비율: {stat[2]/(stat[2]+stat[3]):.2%}')
# print(f'생존자 여성 비율: {stat[3]/(stat[2]+stat[3]):.2%}')

stat = titanic_df.groupby(['Survived', "Sex"]).count()['PassengerId']

# Version 2
print(f"사망자 여성 비율: {stat.loc[(0,'female')]/stat.loc[0].sum():.2%}")
DEAD = 0
SURVIVED = 1
DEAD, SURVIVED = 0, 1
print(f"사망자 여성 비율: {stat.loc[(DEAD,'female')]/stat.loc[0].sum():.2%}")


# stat = titanic_df.groupby(['Survived', "Sex"]).count()['PassengerId']

# print(stat.loc[0, 'female'])


# print(titanic_df.groupby(["Sex"])[["Survived"]].sum())
