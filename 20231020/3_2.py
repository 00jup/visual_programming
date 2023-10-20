def is_prime(num):
    for divider in range(2, num):
        if (num % divider == 0):
            return False
    return True


sum = 0

for i in range(2, 101):
    if (is_prime(i) == True):
        sum += i


print(sum)
