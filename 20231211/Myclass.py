class MyClass:
    a = 10

    def __init__(self, a):
        self.a = a

    @classmethod
    def apply_value(cls, a):
        cls.a = a
        self.a = 100


my_class = MyClass(a=1)
print(my_class.a, MyClass.a)

MyClass.apply_value(a=1)

print(MyClass.a)
print(my)
