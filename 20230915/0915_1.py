import sys

a, b, c = map(int, sys.stdin.readline().split())

if a <= c <= b:
    print((a+b)/2)
elif c < a:
    print(a)
elif b < c:
    print(b)
