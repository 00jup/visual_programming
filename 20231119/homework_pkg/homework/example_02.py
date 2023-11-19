import math


def solve_square_function(a, b, c):
    D = (b ** 2)-(4 * a * c)
    if D >= 0:
        x1 = (-b+math.sqrt(D))/2*a
        x2 = (-b-math.sqrt(D))/2*a
        result = (x1, x2)
        print(result)
    elif D < 0:
        raise Exception("실근 x")
