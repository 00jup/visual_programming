import matplotlib.pyplot as plt
import numpy as np

x = np.random.random((20))
y = np.random.random((5, 20))

fig, ax = plt.subplots()
ax.scatter(x, y[0], s=50, label='y0')
ax.scatter(x, y[1], s=50, label='y1')
ax.scatter(x, y[2], s=50, label='y2')
ax.scatter(x, y[3], s=50, label='y3')
ax.scatter(x, y[4], s=50, label='y4')
ax.set_title("1_assignment")
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_xticks([0, 0.5, 1])
ax.set_yticks([0, 0.5, 1])
plt.show()
