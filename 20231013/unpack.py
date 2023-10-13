nums = (1, 2, 3, 4, 5)
a, *c, b = nums
print(a)  # 출력: 1
print(c)  # 출력: [2, 3, 4]
print(b)  # 출력: 5

print(type(c))

nums = [1, 2, 3, 4, 5]
a, *c, b = nums

print(type(c))
