try:
    raise ArithmeticError
except ArithmeticError:
    print("ArithmeticError occurred")
    raise SyntaxError
except SyntaxError:
    print("SyntaxError")
else:
    print("else\n")

finally:
    print("finished\n\n\n")
