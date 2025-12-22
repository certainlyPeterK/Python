import random

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance
        self.account_number = ''.join([str(random.randint(0, 9)) for i in range(10)])

    def deposit(self, amount):
        self.balance += amount 

    def withdraw(self, amount):
        if (self.balance - amount >= 0):
            self.balance -= amount
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, other_account):
        if (self.balance - amount >= 0 and isinstance(other_account, BankAccount)):
            self.withdraw(amount)
            other_account.deposit(amount)
