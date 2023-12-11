class Dog:
    tricks = []

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.tricks = []
d.add_trick("BARk1")
e.add_trick("BARk2")


print(Dog.tricks)
print(d.tricks)
print(e.tricks)
