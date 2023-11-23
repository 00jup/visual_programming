matrix = []
# with open('make_csv.csv', 'r') as f:
#     data = f.readline()
#     while (data != ''):
#         matrix.append(data)
#         data = f.readline()

# print(matrix)

#####################


# with open('make_csv.csv', 'r') as f:
#     data = f.readline()
#     while (data != ''):
#         row = data.split(",")
#         for index in range(len(row)):
#             row[index] = int(row[index])
#         matrix.append(row)
#         data = f.readline()

with open("make_csv.csv", 'r') as f:
    data = f.readline()
    while (data != ''):
        row = data.split(",")
        for index in range(len(row)):
            row[index] = int(row[index])
        matrix.append(row)
        data = f.readline()

print(matrix)

with open("make_csv.csv", 'r') as f:
    data = f.readline()
    while (data):
        row = data.split('')
        for index in range(len(row)):
            row[index] = int(row[index])
        matrix.append(row)
        data = f.readline()

print(matrix)
