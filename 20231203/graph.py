import numpy as np
import matplotlib.pyplot as plt

data = np.random.random(100)

fig, axes = plt.subplots(1, 4, figsize=(14, 4))
axes[0].hist(data, bins=1)
axes[1].hist(data, bins=5)
axes[2].hist(data, bins=10)
axes[3].hist(data, bins=100)
plt.show()
