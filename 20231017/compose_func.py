def f():
    def g():
        def h():
            nonlocal a
            a = 3
            print("h:", a)
        print("g:", a)
        h()

    a = 1
    print("f:", a)
    g()


a = 0
print("outside:", a)
f()
