class SharedFund:
    deposit = 10000

    def __init__(self, deposit):
        self.deposit = deposit

    def send_class(self, deposit):
        if self.deposit >= deposit:
            self.deposit -= deposit
            SharedFund.deposit += deposit

    def send_instance(self, deposit):
        if SharedFund.deposit >= deposit:
            SharedFund.deposit -= deposit
            self.deposit += deposit


myMoney1 = SharedFund(0)
myMoney2 = SharedFund(0)

myMoney1.send_instance(5000)
myMoney2.send_class(10000)

print(myMoney1.deposit)
print(myMoney2.deposit)
print(SharedFund.deposit)
