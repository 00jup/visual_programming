import numpy as np

a = np.array([1, 2, 3, 4, 5])
print(a)


csv_arr = np.array([1, 2, 3, 4, 5])

np.savetxt('new.csv', csv_arr)
print(np.loadtxt('new.csv'))
