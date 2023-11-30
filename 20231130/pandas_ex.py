import pandas as pd

dft1 = pd.DataFrame({"a": [1., 0, 1], "b": [4, 5, 6], "c": [7, 8, 9]})

print(dft1)
print(dft1.describe())
print(pd.unique(pd.Series([2, 1, 3, 3])))

for index in range(dft1.shape[1]):
    column = dft1.columns[index]
    print(dft1[column])
