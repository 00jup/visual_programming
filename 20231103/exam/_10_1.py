class Tmoney:

    def __init__(self, deposit):
        self.deposit = deposit

    def charge(self, deposit):
        self.deposit += deposit

    def use(self, deposit):
        if self.deposit >= deposit:
            self.deposit -= deposit

    def __repr__(self):
        return self.deposit

    def __str__(self):
        return self.deposit
        # 차이?


class Tmoney2:
    deposit = 0

    @classmethod
    def charge(cls, deposit):
        cls.deposit += deposit

    @classmethod
    def use(cls, deposit):
        if cls.deposit >= deposit:
            cls.deposit -= deposit


a, b = Tmoney(0), Tmoney(0)
c, d = Tmoney2(), Tmoney2()
c.charge(10000)
print(d.deposit)
d.use(1000)
print(c.deposit)

a.charge(10000)
b.charge(10000)

# print(a.deposit)
# print(b.deposit)

# a.use(1000)
# b.use(1000)

# print(a.deposit)
# print(b.deposit)
# print(Tmoney)
