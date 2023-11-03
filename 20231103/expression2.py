class MyClass:

    value = 0

    def __str__(self):
        return "MyClass : " + str(self.value)
## str을 출력하지만 없으면 repr 출력하도록 되어 있구나.. ##


x = MyClass()
# MyClass.value = 1000
x.value = 1000

print(MyClass)
print(MyClass())
print(repr(MyClass()))  # built-in 함수

print(str(MyClass()))
