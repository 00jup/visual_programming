A = list(map(int, input("values ").split()))


def sum(a=0, b=0, c=0):
    print(a+b+c)


sum(*A)
