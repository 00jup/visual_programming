import numpy as np
import pandas


data = pandas.DataFrame(np.random.random((5, 5)),
                        columns=["a", "b", "c", "d", "e"])

# for index in range(data.shape[1]):
#     column = data.columns[index]
# print(data[column])

# print(data.columns[1])

# for column in data:
#     print(column)
#     print(data[column])

# for i, s in data.iterrows():
#     print(i, s, sep='\n')

# print(data.iloc[3])
print(data.loc[:, "a"])
print(data.iloc[:, 0])
# print(data[data > 0.5]

# print(data.sort_values(by="b", ascending=False))
