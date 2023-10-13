import math


def solve(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        return (-b+math.sqrt(D))/2*a, (-b-math.sqrt(D))/2*a
    if D == 0:
        return (-b)/2*a
    else:
        return


a, b, c = map(int, input().split())
print(solve(a, b, c))
