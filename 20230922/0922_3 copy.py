import sys

list = []
list += map(int, sys.stdin.readline().split())
print(list)

numbers = []
sortedList = sorted(list)


for i in range(1, len(list)+1):
    for j in range(1, len(list)+1):
        if sortedList[i] == list[j]:
            numbers[i].append(j)

print(numbers)
