coord = []

for i in range(6):
    given_value = input("좌표를 입력하세요: ")

    x, y = given_value.split(',')
    x = float(x)
    y = float(y)

    coord.append((x, y))

given_value = input("타겟을 입력하세요: ")
x, y = given_value.split(',')
x = float(x)
y = float(y)
target = (x, y)
if target in coord:
    coord.remove(target)

dist_list = []
for point in coord:
    dist = (point[0] - target[0])**2 + (point[1] - target[1])**2
    dist_list.append(dist)

max_dist = max(dist_list)
max_pts = coord[dist_list.index(max_dist)]
print(max_pts)
