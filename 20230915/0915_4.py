# for i in range(101):

sum = 0

# pythonic하게
for numb in range(1, 100 + 1):
    is_prime = False
    # 소수 판별

    # 소수이면 더한다
    if numb == 1:
        is_prime = False
    else:
        for i in range(2, numb):
            if numb % i is 0:
                is_prime = False
                break
        else:
            print(numb)
            # 이렇게 찍으면서 확신을 얻는다.
            is_prime = True

    if is_prime == True:
        sum += numb


print(sum)
