class Bag:
    data = []

    def __init__(self):
        self.data2 = []

    def add(x):
        Bag.data.append(x)

    def addtwice(x):
        Bag.add(x)
        Bag.add(x)


Bag.add(100)
Bag.addtwice(200)

print(Bag.data)
