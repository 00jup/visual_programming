import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.random((100, 3)), columns=['A', 'B', 'C'])
print(data[['A']])
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].scatter(data.index, data[['A']], c='k', s=1, label='1')
axes[1].scatter(data.index, data[['B']], c='r', s=1, label='2')
axes[2].scatter(data.index, data[['C']], c='b', s=1, label='3')

axes[0].set_title("1st Data")
axes[1].set_title("2nd Data")
axes[2].set_title("3rd Data")
plt.tight_layout()

axes[0].fill_between(data.index, 0, data[['A']].mean(), color='k', alpha=0.1)
axes[1].fill_between(data.index, 0, data['B'].mean(), color='k', alpha=0.1)
axes[2].fill_between(data.index, 0, data['C'].mean(), color='k', alpha=0.1)
# 그래프의 미관을 위해 limit 설정
axes[0].set_xlim([0, data.shape[0]-1])
axes[1].set_xlim([0, data.shape[0]-1])
axes[2].set_xlim([0, data.shape[0]-1])
axes[0].set_ylim([0, 1])
axes[1].set_ylim([0, 1])
axes[2].set_ylim([0, 1])
axes[0].legend(loc='upper right')
axes[1].legend(loc='upper right')
axes[2].legend(loc='upper right')

plt.show()
