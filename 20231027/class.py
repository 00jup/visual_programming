class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


Person_instance = Person("park", 10)

# say_hello(Person_instance)

Person_instance.say_hello()
