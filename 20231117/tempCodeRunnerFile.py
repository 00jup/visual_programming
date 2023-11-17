mat = []
with open("test.csv", "r") as f:
    read_data = f.readline()
    while read_data != '':
        row = read_data.split(",")
        for index in range(len(row)):
            row[index] = int(row[index])
        mat.append(row)
        read_data = f.readline()

print(mat)
