from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

# Adjusting the function to match the new expression for Z

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)


def Z_formula(x, y, n_terms=100):
    total = 0
    for n in range(1, n_terms + 1):
        term = 40 * (1 - (-1)**n) / (n * np.pi * np.sinh(n * np.pi))
        term *= np.sin(n * np.pi * x / 5) * np.sinh(n * np.pi * (y / 5))
        total += term
    return total


# Recalculate Z using the new formula
Z_new = np.vectorize(Z_formula)(X, Y)

# Plotting the 3D surface with the updated Z values
fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z_new, cmap=cm.coolwarm)

# Adding a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.title('3D surface plot of Z')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.legend()
# Show the plot
plt.show()
