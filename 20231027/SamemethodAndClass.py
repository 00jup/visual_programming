class Human:

    @classmethod
    def class_method(cls):
        print("클래스 메소드")

    @staticmethod
    def method():
        print("스태틱 메소드")

    def method(self):
        print("인스턴스 메소드")

## 변수랑 다름 똑같지 않다. ##
## 뭐가 뭐를 의미하는지 알 방법이 없다. ##
## 덮어쓰지 않는다. method가 다르기 때문에 ##

## 덮어 쓸 수가 없다. 똑같은 instance를 만드는 것은 덮어쓰지만 ##
## method는 똑같은 이름 실행이 되지 않는다. 그래서 조심하기!! ##
## method가 아닌 함수는 괜찮 def a(self): def a(self): 덮어씀 ##
## 그래서 여기서 method 만들 때 이름을 잘 만들어야 한다.



Human.class_method()
Human.static_method()
Human.instance_method(Human())

me, you = Human(), Human()

me.instance_method()
you.instance_method()
