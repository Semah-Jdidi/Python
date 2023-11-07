class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

class user:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(0.01,0)
    
    def deposit(self, amount):
        self.account.balance += amount
        return self
    
    def withdraw(self, amount):
        self.account.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f'User name: {self.name} \n' f'user balance: {self.account.balance}')
        return self
    
John = user("John")
Adrien = user("Adrien")
Bob = user("Bob")

John.deposit(200).deposit(300).deposit(500).withdraw(400).display_user_balance()

Adrien.deposit(200).deposit(200).withdraw(100).withdraw(50).display_user_balance()

Bob.deposit(2000).withdraw(250).withdraw(150).withdraw(200).display_user_balance()