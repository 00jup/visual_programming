
with open("test.txt", "w") as f:
    f.write("Hello world!\n")

with open("test.txt", "r") as f:
    print(f.readline())

with open("test.txt", "a") as f:
    f.write("return")

with open("test.txt", "r") as f:
    print(f.read())
