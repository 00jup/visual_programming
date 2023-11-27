import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(a)

print(a[1:3, :])
print(a[1:3, 0:2])
print(a[1:3, 0:1])

print(a[a < 5])

five_up = (a >= 5)
print(a[five_up])

print(np.random.random((3, 2)))
print(np.ones(2))

print("--------------------")
print()
print()
print(np.zeros(2))
print(np.empty((2)))
print(np.empty((2, 1)))
print(np.empty((2, 3)))
print("--------------------")
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(np.concatenate((x, y), axis=1))
z = np.concatenate((x, y), axis=0)
print("--------------------")
print(z.reshape(4, 2))
