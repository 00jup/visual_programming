a = 1


def f():
    a = 11

    def g():
        a = 21

        def r():
            nonlocal a
            a = 31
            print(a)
        r()
        print(f"g : {a}")
    g()
    print(f"f : {a}")


f()
print(f"out : {a}")
