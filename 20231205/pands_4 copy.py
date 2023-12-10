import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = [a for i in range(2)]
a[0] += 10
b[0][2] += 10
print(f'\n[7. Numpy multiply by list comprehension]')
print(f'{a=} # Weird')  # [11,  2,  13,  4,  5]
print(f'{b=} # Weird')  # [[11,  2, 13,  4,  5], [11,  2, 13,  4,  5]]
## 다 연결됨 ##

a = np.array([1, 2, 3, 4, 5])
b = np.array([a for i in range(2)])
a[0] += 10
b[0, 2] += 10
print(f'\n[7. Numpy multiply by list comprehension]')
print(f'{a=} # Not weird')  # [11,  2,  3,  4,  5]
print(f'{b=} # Not weird')  # [[ 1,  2, 13,  4,  5], [ 1,  2,  3,  4,  5]]
## 새로운 객체가 만들어짐 ##

a = np.array([1, 2, 3, 4, 5])
b = np.array([a for i in range(2)])
a[0] += 10
b[0][2] += 10
print(f'\n[8. Numpy multiply by list comprehension and convert as numpy]')
print(f'{a=} # Not weird')  # [11,  2,  3,  4,  5]
print(f'{b=} # Not weird')  # [[ 1,  2, 13,  4,  5], [ 1,  2,  3,  4,  5]]
