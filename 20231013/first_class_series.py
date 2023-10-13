def function():
    print("HHHHH")


def function2(f):
    f()


function2(function)


def function(name):
    if name == "abs":
        return abs
    elif name == "int":
        return int
    elif name == "len":
        return len

## C도 가능함. -> 함수 포인터 개념 ##


print(function("len")("111111"))

f = function

print(f("len")("111111"))


def f(x): return x + 1


print(f(1))


def f(x, y): return x+y
# 이거 잘 안 쓰려고 함.


print(f(1, 2))
# 유용하긴 함.
