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
        if numb % i == 0:
            print("소수가 아닙니다.")
            break
    else:
        print("소수입니다.")
