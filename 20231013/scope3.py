def f():
    def g():
        def h():
            nonlocal a
            print("h", a)
        a = 2
        print("g", a)
        h()
    a = 1
    print("f", a)
    g()


a = 0
print("global", a)

f()
