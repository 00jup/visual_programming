# print(f"int: {1}")
# print(f"float: {1.0}")
# print(f"bool: {True}")

# A = 10

# print(f"int: {A:+}")
# A = -10
# print(f"int: {A:-}")

# print(f"float: {A:.2f}")


# file = open("test1234.txt", "+w")
# file.write("test")
# file.close()

# file = open("test1234.txt", "r")
# print(f"file: {file}")
# file.readline()
# file.close()

# with open("tes &t1234.txt", "w") as f:
#     f.write("test\n")
#     f.write("test\n")

# with open("test1234.txt", "r") as f:
#     print(f.readline())
#     print(f"file: {f}")

with open('assign.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9 10\n')


with open('assign.txt', 'a') as f:
    f.write("hello\n")


with open('assign.txt', 'r') as f:
    read_data = f.readline()
    while read_data != '':
        print(read_data, end='')
        read_data = f.readline()
