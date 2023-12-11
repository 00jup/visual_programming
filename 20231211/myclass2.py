class MyClass:
    a = 10

    def __init__(self, n):
        self.b = n

    def __str__(self):
        return f'a:{MyClass.a}, b:{self.b}'

    @staticmethod
    def add(x):
        MyClass.a += x


x = MyClass(20)
print(x)

x.add(10)

print(x)
