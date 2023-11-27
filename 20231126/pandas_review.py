import pandas as pd
import numpy as np

# s = pd.Series(pd.random.randn(5), name="something")
s = pd.Series([1, 2, 3, 4, 5, 5])
print(s)

d = {"one": [1, 2, 3, 4, 4], "two": [1, 2, 3, 4, 4]}

print(pd.DataFrame(d))

print(s.dtypes)

data = pd.DataFrame(np.random.random((4, 4)),
                    columns=['A', 'B', 'C', 'D'])

print("---------start------------")
print(data)
print()
print()
# DataFrame의 열 개수를 바탕으로 column 접근
for index in range(data.shape[1]):
    column = data.columns[index]
    print(data[column])
print("---------------------------------1")
# for문을 통해 column에 직접 접근
for column in data:
    print(column)
    print(data[column])
print("---------------------------------2")
# data.iterrows()를 통해 각 행에 직접 접근
for index, series in data.iterrows():
    print(index, series)
print("---------------------------------3")
# data.items()를 통해 각 열에 직접 접근
for index, series in data.items():
    print(index, series)
print("---------------------------------4")


print(df.)