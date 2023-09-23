import sys

points = ()
for _ in range(5):
    a, b = map(float, sys.stdin.readline().split())
    points = points + ((a, b),)
    # points = points + ((a, b)) 둘은 다르다
print(points)
center = []
# center = center + (sum(sub)/len(sub) for sub in points)
center = (sum(sub)/len(sub) for sub in points)
print(center)

distance = ()
for _ in range(5):
    distance = distance + (tuple((center*sub) ^ 2 for sub in points))

for dis in distance:
    print(dis)


# 기능 다 외우기