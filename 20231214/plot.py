import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

data = {"A": range(1, 51), "B": np.random.random(50)}

fig, ax = plt.subplots()
ax.plot("A", "B", c="r", marker="o", ls=":", data=data)

plt.show()
