
# n 넣어야 함.

def is_prime(number):
    for divider in range(2, number):
        if number % divider:
            return False
    return True
    # else:
    #     return True


given_value = int(input())
count = 0
for value in range(1, given_value+1):
    if is_prime(value):
        count += 1

print(100)
