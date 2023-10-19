## 에어컨 온도를 지정해라 ##
## 이런 건 풀어놓는다. ##
# f(18, arg = ) 개발자들만 아는 키워드를 넣어서 동작하도록 만들 때 필요함 숨겨놓고 공유해서 쓴다.abs
# 수학계산, 머신러닝에서 많이 쓴다.
# f g h l   f -> 에서는 쓰지 않고 아래에서 쓸 때 임. bypassing


def f(a, /):
    print(a)


f(1)


def f(b, /, a):
    print(a)


f(1, a=1)


def f(*, a, b, c):
    print(a, b, c)


f(a=1, b=2, c=3)

### 생략된 게 아니라 default값입 ###

# 그러면 평소에 f(/, ,*) 이렇게 생략되어 있다고 생각해도 되나? #


def f(a, b, c, /, *, d):
    print(a, b, c, d)


f(1, 2, 3, d=4)
