def f(a, /, b, *, c):
    print(a, b, c)


f(1, b=2, c=3)
f(1, 2, c=3)
