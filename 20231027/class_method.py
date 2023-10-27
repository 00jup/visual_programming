class Human:

    @classmethod
    def class_method(cls):
        print("클래스 메소드")

    @staticmethod
    def static_method():
        print("스태틱 메소드")

    def instance_method(self):
        print("인스턴스 메소드")


Human.class_method()
Human.static_method()
Human.instance_method(Human())
