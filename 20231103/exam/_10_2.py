class SharedFund:
    deposit = 10000

    def __init__(self, deposit):
        self.deposit = deposit

    def save(self, deposit):
        if self.deposit >= deposit:
            self.deposit -= deposit
            SharedFund.deposit += deposit

    def withdraw(self, deposit):
        if SharedFund.deposit >= deposit:
            SharedFund.deposit -= deposit
            self.deposit += deposit


myMoney1 = SharedFund(0)
myMoney2 = SharedFund(0)

myMoney1.withdraw(5000)
myMoney2.save(10000)

print(myMoney1.deposit)
print(myMoney2.deposit)
print(SharedFund.deposit)

## 사람에게 30개 정도의 아이템을 배분한다. 공용 자산을 얼마나 빨리가져가게 하는지 티켓팅이 가능해진다. ##
## deposit 구조로 ticketing을 구현할 수 있다. ##


class Ticketing:
    seat_number_list = list(range(1, 31))

    def __init(self):
        self.seat_number = None

    def book(self):
        if self.seat_number == None:
            self.seat_number = Ticketing.seat_number_list.pop(0)
            return self.seat_number


a = Ticketing()
print(a.book())
