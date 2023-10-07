import random

list = []
for i in range(1, 101):
    list.append(i)

random.shuffle(list)

print(list[0:10])
