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
# DataFrame의 열 개수를 바탕으로 column 접근
for index in range(data.shape[1]):
    column = data.columns[index]
    print(data[column])