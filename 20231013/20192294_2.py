

def is_prime(number):
    for divider in range(2, number):
        if number % divider == 0:
            return False
    return True


given_value = int(input())
count = 0
for value in range(2, given_value+1):
    if is_prime(value):
        count += 1

print(count)
