import sys

a = int(sys.stdin.readline())

while (1):
    if a > 10000:
        a = int(sys.stdin.readline())
    else:
        break

print(a)
