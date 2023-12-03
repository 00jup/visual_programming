import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.random((10, 7)), columns=[
                    'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])


fig, axes = plt.subplots()
for column in data.columns:
    axes.plot(data.index, data[[column]], marker='v')

axes.set_xlim([0, 6])
axes.set_xticks([0, 1, 2, 3, 4, 5, 6], [
    'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

max = data.max(axis=0).max()
min = data.min(axis=0).min()
mean = (max+min)/2

axes.axhline(max)
axes.axhline(mean)
axes.axhline(min)

axes.set_yticks([max, mean, min], ['max', 'mean', 'min'])
plt.show()
9