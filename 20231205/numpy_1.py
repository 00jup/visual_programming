import numpy as np

# input_array = list(map(int, input("12개의 숫자 입력 : ").split()))
input_array = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

input_array = np.array(input_array).reshape(3, 4)
avg_array = input_array.mean(axis=1)

count = np.ones((input_array.shape[0], 1))


for index in range(input_array.shape[0]):
    new_data = input_array[index]
    count[index] = new_data[new_data > avg_array[index]].size

print(count)
