# 개념과 외형

class Human:

    number_of_arms = 2

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


me = Human("park", 60)
print(me.name, me.weight)

print(me.number_of_arms)

me.number_of_arms = 3

print(me.number_of_arms)

me2 = Human("kim", 70)

print(me2.number_of_arms)
