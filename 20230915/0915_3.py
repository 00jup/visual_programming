import sys

numb = int(sys.stdin.readline())

while (1):
    if numb > 10000:
        numb = int(sys.stdin.readline())
    else:
        break

if numb == 1:
    print("소수입니다.")
else:
    for i in range(2, numb):
        if numb % i is 0:
            print("소수가 아닙니다.")
            break
    else:
        print("소수입니다.")


# pythonic하게
for divider in range(2, numb):
    if numb % divider == 0:
        print('no')
        break
else:
    print("prime")

if numb == 1:
    is_prime = False
else:
    for i in range(2, numb):
        if numb % i is 0:
            is_prime = False
            break
    else:
        is_prime = True


