class MyClass:
    value = 'MyClass'

    def __init__(self):
        self.value = 'MyClass instance'

    class MyInnerClass:
        value = 'MyInnerClass'

        def __init__(self):
            self.value = 'MyInnerClass instance'


print(MyClass.value)                      # 'MyClass instance'
print(MyClass.MyInnerClass.value)         # 'MyInnerClass'
## 클래스의 변수 ##
print(MyClass.MyInnerClass().value)       # 'MyInnerClass instance'
## 수강생 1이라는 실체. 이건 instance임 그래서 intance의 변수라는 것을 확실히 알 수 있다. ##

print(MyClass().value)
print(MyClass().MyInnerClass.value)
print(MyClass().MyInnerClass().value)
