import numpy as np
import matplotlib.pyplot as plt

x = np.arange(10, 15)
y = np.random.random(5)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
