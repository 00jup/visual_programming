import math

a, b, c = map(int, input("a, b, c 입력 : ").split())


def solve_square_function(a, b, c):
    D = (b ** 2)-(4 * a * c)
    try:
        x1 = (-b+math.sqrt(D))/2*a
        x2 = (-b-math.sqrt(D))/2*a
        print(f"({x1},{x2})")
    except D < 0:
        print("근이 없습니다.")
