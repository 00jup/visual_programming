class MyClass:
    value = 0

    def __repr__(self):
        return '@MyClass: ' + str(self.value)


x = MyClass()
print(MyClass)     # 출력: <class '__main__.MyClass'>
print(MyClass())   # 출력: @MyClass: 1000 (이 출력 결과는 value 값에 따라 변경될 수 있음)
print(repr(MyClass()))   # 출력: @MyClass: 1000
print(str(MyClass()))    # 출력: @MyClass: 1000
print()


class MyClass:
    value = 0

    def __str__(self):
        return 'MyClass: ' + str(self.value)


x = MyClass()
print(MyClass)     # 출력: <class '__main__.MyClass'>
print(MyClass())   # 출력: MyClass: 1000
# 출력: <__main__.MyClass object at 0x7f9...> (이 주소 값은 실행할 때마다 변경될 수 있음)
print(repr(MyClass()))
print(str(MyClass()))    # 출력: MyClass: 1000
