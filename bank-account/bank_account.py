import threading

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.opened = False
        self.lock = threading.Lock()

    def get_balance(self):
        if self.opened: 
            return self.balance
        else:
            raise ValueError("Not opened")

    def open(self):
        if self.opened: 
            raise ValueError("Already opened")
        else:
            self.opened = True
            self.balance = 0
        
    def deposit(self, amount):
        with self.lock:
        
            if amount >= 0 and self.opened:
                self.balance += amount
            else:
                raise ValueError("Account not opened or invalid amount")
        
        #self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        
        if self.opened and (amount >= 0) and (amount <= self.balance):
            self.balance -= amount
        else:
            raise ValueError("Account not opened or invalid amount")
        
        self.lock.release()

    def close(self):
        if self.opened:
            self.opened = False
        else:
            raise ValueError("Already closed")
