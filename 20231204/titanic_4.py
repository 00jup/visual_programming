import pandas as pd
import numpy as np

# stat = data.groupby(['Survived', "Sex"]).sum()['Fare']
# count = data.groupby(['Survived', "Sex"]).count()['Fare']

# print(stat[0]['female'])
# print(stat[0]['male'])
# print(stat[1]['female'])
# print(stat[1]['male'])

data = pd.read_csv("titanic.csv")
# print(data)

data["Age-Range"] = np.floor(data["Age"]/10)*10
data = data[["Age-Range", "Survived", "Fare"]].dropna()
data = data.astype({"Age-Range": int})

data = data.groupby(["Survived", "Age-Range"]).mean()
# data = data.groupby(["Survived", "Age-Range"]).mean()['Fare']

# for i in data:
# print(f"{i}\n")

# print(data.dtypes)


# Version 1 처음 공부할 때는 이렇게 짬
new_data = pd.DataFrame(index=[0, 10, 20, 30, 40, 50, 60, 70, 80],
                        columns=["Dead", "Survived"])

new_data['Dead'] = data.loc[0]
new_data['Survived'] = data.loc[1]

new_data = new_data.fillna(value=0)


# Version 2 pivot table, 배우면 간단하게 한줄로 이렇게 짤 수 있다.
# 나중에 필요하면 공부해보기
new_data2 = data.pivot_table(index='Age-Range',
                             columns=["Survived"],
                             values="Fare",
                             aggfunc='mean')  # .melt()
# value가 왜 빠진 거지?
print(new_data2)
new_data.to_csv("result.csv")
# print(pd.read_csv("result.csv"))
