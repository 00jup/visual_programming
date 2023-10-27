class Dog:
    kind = 'caine'

    def __init__(self, name):
        self.name = name


d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)
print(e.kind)

print(d.name)
print(e.name)
