import numpy as np
import random
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 1000)

a, b, c, d = random.sample(range(1, 10), 4)


# np.random.random(1)

fig, axes = plt.subplots()
axes.scatter(x, a*x+b, label='x')
axes.scatter(x, a*(x**2)+b*x+c, label='x2')
axes.scatter(x, a*(x**3)+b*(x**2)+c*x + d, label='x3')
axes.legend()
plt.tight_layout()

plt.show()
