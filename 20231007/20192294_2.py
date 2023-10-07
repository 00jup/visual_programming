import random
import sys


base_list = []

for number in range(1, 46):
    base_list.append(number)

random.shuffle(base_list)
lotto_value = base_list[:6]

## user input ##

# given_values = map(int, sys.stdin.readline().split())

given_values = input("로또 번호를 입력하시오. : ").split()

count = 0
for i in range(6):
    given_values[i] = int(given_values[i])

    if given_values[i] in lotto_value:
        count += 1

print(lotto_value)
print(count)
