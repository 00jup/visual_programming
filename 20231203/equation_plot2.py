import numpy as np
import random
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 1000)

a, b, c, d = random.sample(range(1, 10), 4)


# np.random.random(1)

fig, axes = plt.subplots(1, 3)
axes[0].plot(x, a*x+b)
axes[1].plot(x, a*(x**2)+b*x+c)
axes[2].plot(x, a*(x**3)+b*(x**2)+c*x + d)

plt.show()
