class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        if self.opened: 
            return self.balance
        else:
            raise ValueError

    def open(self):
        self.opened = True

    def deposit(self, amount):
        if amount >= 0 and self.opened:
            self.balance += amount
        else:
            raise ValueError

    def withdraw(self, amount):
        if self.opened and (amount >= 0) and (amount <= self.balance):
            self.balance -= amount
        else:
            raise ValueError

    def close(self):
        if self.opened:
            self.opened = False
            self.balance = 0
        else:
            raise ValueError
