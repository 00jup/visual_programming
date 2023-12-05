import numpy as np

random_array = np.random.random((10, 10))
np.savetxt("data.csv", random_array)

read_array = np.loadtxt("data.csv")

result = np.ones((5, 5))
for i in range(5):
    for j in range(5):
        result[i][j] = read_array[2*i:2*(i+1), 2*j:2*(j+1)].sum()

result = np.sort(result, axis=0)
print(result)
np.savetxt("sorted_data.csv", result)
