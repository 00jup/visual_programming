class MyClass:

    value = 0

    def __repr__(self):
        return "@MyClass : " + str(self.value)


x = MyClass()
# MyClass.value = 1000
x.value = 1000

print(MyClass)
print(MyClass())
print(repr(MyClass()))  # built-in 함수

print(str(MyClass()))
