N = int(input("input : "))


def is_prime(number):
    for divider in range(2, N):
        if number % divider == 0:
            return False
    return True


print(is_prime(N))
