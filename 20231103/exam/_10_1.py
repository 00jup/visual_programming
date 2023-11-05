class Tmoney:

    def __init__(self, deposit):
        self.deposit = deposit

    def charge(self, deposit):
        self.deposit += deposit

    def use(self, deposit):
        self.deposit -= deposit

    def __repr__(self):
        return self.deposit


a, b = Tmoney(0), Tmoney(0)

a.charge(10000)
b.charge(10000)

print(a.deposit)
print(b.deposit)

a.use(1000)
b.use(1000)

print(a.deposit)
print(b.deposit)
