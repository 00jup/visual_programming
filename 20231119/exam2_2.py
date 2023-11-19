import math

a, b, c = map(int, input("a, b, c 입력 : ").split())


def solve_square_function(a, b, c):
    D = (b ** 2)-(4 * a * c)
    if D >= 0:
        x1 = (-b+math.sqrt(D))/2*a
        x2 = (-b-math.sqrt(D))/2*a
        result = (x1, x2)
    elif D < 0:
        raise Exception("실근 x")

    return result


print(solve_square_function(a, b, c))
