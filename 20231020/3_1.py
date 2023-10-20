def is_prime(num):
    for divider in range(2, num):
        if (num % divider == 0):
            return False
    return True


num = int(input("숫자 입력"))


print(is_prime(num))
