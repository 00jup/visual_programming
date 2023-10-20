total = 0
for number in range(9, 11, 2):
    index = 0
    while index < int(number/2):
        value = index % 3
        match value:
            case 0 if index != 0:
                total += 1
            case 1:
                total += 2
            case 2:
                total += 3

        index += 1

print(total)
