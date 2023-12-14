import numpy as np

ex = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])

print(ex.mean(axis=0))
print(ex.mean(axis=1))
