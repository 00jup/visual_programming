import math


def f(g, a, b, c, x):
    return g(a, b, c, a*(x**2) + b*x + c)


def g(a, b, c, x):
    return a*math.sin(b*x) + c


values = input().split()
for i in range(len(values)):
    values[i] = float(values[i])

# for value in values:
#     print(f(float(value), 1, 2, 3), end=' ')

print(f(g, *values))
# 잘못한 부분 있음.

# def f(a, b, c, x), a:???????????
