matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
with open("make_csv.csv", "w") as f:
    for row in matrix:
        f.write(f'{row[0]},{row[1]},{row[2]}\n')

with open("make_csv.csv", "r") as f:
    read_data = f.readline()
    while (read_data != ''):
        print(read_data, end="")
        read_data = f.readline()
