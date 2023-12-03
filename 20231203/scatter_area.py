import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.random((100, 3)), columns=['A', 'B', 'C'])
print(data[['A']])
fig, axes = plt.subplots(1, 3)
axes[0].scatter(data.index, data[['A']], c='k', alpha=0.1)
axes[1].scatter(data.index, data[['B']], c='k', alpha=0.1)
axes[2].scatter(data.index, data[['C']], c='k', alpha=0.1)

plt.show()
