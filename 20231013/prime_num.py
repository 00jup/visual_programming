import math

N = round(float(input()), 3)
N = int((N-int(N))*1000)


def is_prime(num):
    for divider in range(2, num):
        if num % divider == 0:
            return False
    return True


def f_prime(N):
    for num in range(2, N):
        if is_prime(num) == True:
            result = num

    print(result)


f_prime(N)
