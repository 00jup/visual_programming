import math


def f(a, b, c, x):
    return a*(x**2) + b*x + c


def g(a, b, c, n):
    return a*(math.sin(b*n))+c


values = list(map(int, input().split()))

print(f(*values[:3], g(*values)))
