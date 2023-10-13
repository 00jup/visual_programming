# def g():
#     a = 1

#     def f():
#         g()
#         print(a)


# f()
# g()
# print(a)

def f():
    def g():
        a = 1
        print(a)
    # g()
    # print(a)
    g()


f()
# f(g) -> 불가능함.
# g() -> f 안에서만 적용되어 있어서 쓸 수 없다.

f(g())
