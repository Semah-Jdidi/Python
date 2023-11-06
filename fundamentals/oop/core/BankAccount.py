class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f'Balance : {self.balance}')

    def yield_interest(self):
        if self.balance > 0 :
            self.balance +=  self.balance * self.int_rate
        return self

John = BankAccount(0.01,0)
Sadie = BankAccount(0.01,0)

John.deposit(500).deposit(200).deposit(50).withdraw(100).yield_interest().display_account_info()
Sadie.deposit(1000).deposit(1000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()