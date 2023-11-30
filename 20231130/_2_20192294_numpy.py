import random
import numpy as np

list = []
for i in range(1, 101):
    list.append(i)

random.shuffle(list)

list = np.array(list).reshape(10, 10)


np.savetxt('data.csv', list)

new_data = np.loadtxt('data.csv')

sum_data = np.zeros((5, 5))

for i in range(5):
    for j in range(5):
        sum_data[i, j] = new_data[i, j] + new_data[i+1, j+1] + \
            new_data[i+1, j] + new_data[i, j+1]


print(sum_data)
sum_data = np.sort(sum_data, axis=0)
print()
print(sum_data)
np.savetxt('sorted_data.csv', sum_data)
