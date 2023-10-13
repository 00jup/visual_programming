# scanf와 printf는 왜 여러개의 인자를 받을 수 있는 거지? va_list와 같은 구조체를 만들어서 처리함.abs

# python에서는 함수 자체에서 기능을 제공함.

# packing ## 이건 함수고
def f(*c):
    print(c)


f(1, 2, 3)


a, *b, c = [1, 2, 3, 4, 5]
print(a, b, c)

# a, **b, c = [1, 2, 3, 4, 5]  이건 함수가 아닌 것임
print(a, b, c)

#### 여기서는 list 들어가는데 다른 건가? ####


def f(**c):
    print(c)


f(a=1, b=2, c=3)


def f(*x):
    return x[0] + x[1]**2
    # Tuple이니까 가능함.a


print(f(1, 2, 3))
