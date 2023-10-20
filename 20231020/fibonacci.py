number = int(input())


def fibonacci(count):
    a = 0
    b = 1
    for i in range(0, count):
        print(a, end=" ")
        a, b = b, a+b


fibonacci(number)
print()
A = 2
B = 0

if A:
    print(A)
elif not B:
    print(B)


if not B:
    print(B)
