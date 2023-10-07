import random

a = list(range(1, 101))

b = set(range(1, 51))
count = 0

for _ in range(100):
    random.shuffle(a)
    a_sliced = set(a[:5])
    # a = set(a)
    if a_sliced <= b:
        count += 1

print(count)
