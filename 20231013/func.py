def return_func(a):
    return print(a+1)


def greet(a):
    a += 1
    return a


a = 10
return_func(greet(a))
