import numpy as np
import random
# array = list(map(int, input("12개의 숫자 입력 : ").split()))
# array = random.sample(range(1, 13), 12)
array = np.random.random(12)
# b = np.arange(*array)
array = np.array(array)
array = np.sort(array)
array = array.reshape(3, 4)
print(array)
avg = np.average(array, axis=1)
print(avg)
# for i in avg:
#     print(array[array > i])

# sum_array = np.sum(array, axis=1)
# print(sum_array)
for i in range(len(array)):
    for j in range(len(array[i])):
        # print(array[array[i] > avg])
        pass

# result = np.reshape(3, 1)
result = np.zeros(array.shape[0])

for index in range(array.shape[0]):
    new_data = array[index]
    result[index] = new_data[new_data > avg[index]].size

print(result)

# for index in range(array.shape[0]):
#     new_data = array[index]
#     new_data[new_data > avg[index]] = 1
#     new_data[new_data < avg[index]] = 0
#     print(new_data)
#     print(index)
#     result[index] = new_data.sum()
# print(result)


print(np.zeros((3, 1)))
print(np.zeros((1, 3)))
print(np.zeros(3))
