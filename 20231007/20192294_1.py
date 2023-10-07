import random

base_list = []

for number in range(1, 101):
    base_list.append(number)

random.shuffle(base_list)

print(base_list[:10])
