class MyClass:
    value = 0

    def __init__(self):
        print("I'm born!\n")

    def __del__(self):
        print("I'm dead!\n")


x = MyClass()
print(MyClass())

del x
print("End of program")
