import sys

a, b, c = map(int, sys.stdin.readline().split())

if c < a:
    print(a)
elif c > b:
    print(b)
else:
    print((a+b)/2)
