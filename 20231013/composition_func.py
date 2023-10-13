import math


def f(a, b, c, x):
    return a*(x**2) + b*x + c


def g(a, b, c, x):
    return a*math.sin(b*x) + c


values = input().split()

for i in range(len(values)):
    values[i] = float(values[i])

# for value in values:
#     value = float(value)
#     print(f(float(value), 1, 2, 3), end=' ')

# print(f(g(*values), 1, 2, 3))


# print(*values[:3])
print(f(*values[:3], g(*values)))


# def f(a, b, c, x), a:???????????
