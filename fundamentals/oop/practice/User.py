class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def deposit(self, amount):
        self.account_balance += amount
        return self
    
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f'User name: {self.name} \n' f'user balance: {self.account_balance}')
        return self

user_1 = user("John","John@gmail.com")
user_2 = user("Adrien","John@gmail.com")
user_3 = user("Bob","John@gmail.com")

user_1.deposit(200).deposit(300).deposit(500).withdraw(400).display_user_balance()

user_2.deposit(200).deposit(200).withdraw(100).withdraw(50).display_user_balance()

user_3.deposit(2000).withdraw(250).withdraw(150).withdraw(200).display_user_balance()
