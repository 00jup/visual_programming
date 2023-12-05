import pandas as pd
import numpy as np

# titanic_df = pd.read_csv("titanic.csv")
# print(titanic_df)

# titanic_df = titanic_df[["Age", "Survived", "Fare"]].dropna()
# titanic_df["Age-Range"] = np.floor(titanic_df["Age"]/10)*10
# fare = titanic_df.groupby(["Survived", "Age-Range"]).sum["Fare"]
# count = titanic_df.groupby(["Survived", "Age-Range"]).count["Fare"]

# print(fare)

# stat = titanic_df.groupby(['Survived', "Sex"]).sum()['Fare']
# count = titanic_df.groupby(['Survived', "Sex"]).count()['Fare']

# print(stat[0]['female'])
# print(stat[0]['male'])
# print(stat[1]['female'])
# print(stat[1]['male'])

filename = 'titanic.csv'

data = pd.read_csv(filename)
data = data[data['Survived'] == 1]
data = data[['Age']].dropna()
data["Age-band"] = np.floor(data['Age']/10)*10
# int(data['Age']/10)은 숫자 하나를 바꿔주는 거임. --> broadcasting 되니까 int가 아니라 np.floor로 진행해야 함
data = data.astype({'Age-band': int, 'Age': int})
# data.groupby('Age-band').count().rename({'Age': 'count'}, axis=1)
print(data.groupby('Age-band').count())
