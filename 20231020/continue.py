numbers = [x for x in range(1, 11)]
sum = 0


for i in numbers:
    if int(i) % 2 == 0 or int(i) % 3 == 0:
        continue
    sum += i

print(sum)


my_set = {1, 2, 4}
print(my_set)

print()
print(numbers[:])
numc = [1, 2, 3, 4, 5]
print(numc[0:4:2])
