import numpy as np

array = list(map(int, input("12개의 숫자 입력 : ").split()))
# b = np.arange(*array)
array = np.array(array)
array = array.reshape(3, 4)

print(array)
avg_arr = np.average(array, axis=0)
print(avg_arr)

sum_array = np.sum(array, axis=0)
print(sum_array)

