
class Account:
    money = 100000

    def __init__(self):
        self.money = 0

    def get_total_deposit_static(self):
        return Account.money

    @classmethod
    def get_total_deposit(cls):
        return cls.money
    
    def get_my_deposit(self):
        return self.money
        
book = Account()