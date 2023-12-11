import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.random((4, 4)), columns=["A", "B", "C", "D"])

# for i in range(data.shape[0]):
#     print(data.iloc[i])

# for column in data:
#     print(data[column])

# for index, columns in data.items():
#     print(columns)

# for index, columns in data.iterrows():
#     print(columns)

print(data[data.columns[0]])
