

try:
    print(1/0)
    raise ArithmeticError
except TypeError:
    print("Type error occurred!")
except ArithmeticError:
    raise ArithmeticError("이상한 에러")
    print("ArithmeticError")
