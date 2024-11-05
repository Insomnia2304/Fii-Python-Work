class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print('Insufficient funds')
        else:
            self.balance -= amount
    
    def __str__(self):
        return f'{self.name}: {self.balance}'
    
class SavingsAccount(Account):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def __str__(self):
        return f'{self.name}: {self.balance} (interest rate: {self.interest_rate})'
    
class CheckingAccount(Account):
    def __init__(self, name, balance, maintenance_fee):
        super().__init__(name, balance)
        self.maintenance_fee = maintenance_fee
    def deduct_maintenance_fee(self):
        self.balance -= self.maintenance_fee
    def __str__(self):
        return f'{self.name}: {self.balance} (maintenance fee: {self.maintenance_fee}){"" if self.balance >= 0 else " (overdraft)"}'

accounts = [SavingsAccount('Alice', 1000, 0.01), CheckingAccount('Bob', 500, 5)]
for account in accounts:
    print(account)
    account.deposit(100)
    account.withdraw(50)
    if isinstance(account, SavingsAccount):
        account.add_interest()
    if isinstance(account, CheckingAccount):
        account.deduct_maintenance_fee()
    print(account)
    