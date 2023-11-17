list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

with open("test.csv", "w") as f:
    for row in list:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")

with open("test.csv", "r") as f:
    # print(f.read()) 이것도 안 좋은 습관이 될 수 있다.
    output = f.readline()
    while output:
        print(output, end="")
        output = f.readline()
