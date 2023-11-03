class Account:
    money = 100000

    def __init__(self, money):
        self.money = money
    # def __init__(self):
    #     self.money = 0

    def get_total_deposit_static():
        return Account.money

    @classmethod
    def get_total_deposit(cls):
        return cls.money

    def get_my_deposit(self):
        return self.money


book = Account(1000)

print(book.get_my_deposit())
