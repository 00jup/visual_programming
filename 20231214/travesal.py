import numpy as np
import pandas as pd

data = pd.DataFrame(np.random.random((10, 4)), columns=["A", "B", "C", "D"])

# for i in range(data.shape[0]):
#     print(data.iloc[i])

# for column in data:
#     print(data[column])

# for column, series in data.items():
#     print(series)
# for row, series in data.iterrows():
#     print(series)

# for index in range(data.shape[1]):
#     print(data[data.columns[index]])
# print(data.index)

print(data[(data["A"] > 0.5) & (data["B"] < 0.7)])
