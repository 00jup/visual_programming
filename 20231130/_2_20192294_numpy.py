import random
import numpy as np

data = []
for i in range(1, 101):
    data.append(i)

random.shuffle(data)

data = np.array(data).reshape(10, 10)


np.savetxt('data.csv', data)

data = np.loadtxt('data.csv')

sum_data = np.zeros((5, 5))
# version1
for index in range(sum_data.shape[0]):
    data[index] = data[2*index:2*index+1].sum(axis=0)

for index in range(sum_data.shape[1]):
    data[:, index] = data[:, 2*index:2*index+1].sum(axis=1)

print(data[:5, :5])

# for i in range(5):
#     for j in range(5):
#         sum_data[i, j] = new_data[i, j] + new_data[i+1, j+1] + \
#             new_data[i+1, j] + new_data[i, j+1]

# version2
for i in range(5):
    for j in range(5):
        sum_data[i, j] = data[2*i:2*i+1, 2*j:2*j+1].sum(axis=1)
        sum_data[i, j] = data[2*i:2*i+1, 2*j:2*j+1].sum(axis=0)

print(sum_data == data[:5, :5])


# print(sum_data)
sum_data = np.sort(sum_data, axis=0)
# print()
print(sum_data)
# np.savetxt('sorted_data.csv', sum_data)
