import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.random((100000, 3)), columns=['A', 'B', 'C'])

fig, axes = plt.subplots(1, 3, figsize=(12, 4))

for index in range(data.shape[1]):
    # 열의 개수만틈 보고 반복할 것임 0 1 2
    axes[index].scatter(data.index, data[data.columns[index]],
                        c='k', s=1, alpha=0.1)

    axes[index].fill_between(
        data.index, 0, data[data.columns[index]].mean(), color='k', alpha=0.1)
    # 그래프의 미관을 위해 limit 설정
    axes[index].set_xlim([0, data.shape[0]-1])
    axes[index].set_ylim([0, 1])
    axes[index].set_yticks([0, 0.5, 1])

plt.show()
