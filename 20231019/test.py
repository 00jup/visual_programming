print(type(4/2))
print(4/2)
print(type(10 % 3))

i = 0

while True:
    if i >= 5:
        break
    if i == 1:
        i += 1
        continue
    i += 1

    print(i)


a = 2
b = 3
print()
print(a if a > b else b)
