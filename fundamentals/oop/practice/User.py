class user:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def deposit(self, amount):
        self.account_balance += amount  
    
    def withdraw(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f'User name: {self.name} \n' f'user balance: {self.account_balance}')

user_1 = user("John","John@gmail.com")
user_2 = user("Adrien","John@gmail.com")
user_3 = user("Bob","John@gmail.com")

user_1.deposit(200)
user_1.deposit(300)
user_1.deposit(500)
user_1.withdraw(400)

user_1.display_user_balance()

user_2.deposit(200)
user_2.deposit(200)
user_2.withdraw(100)
user_2.withdraw(50)

user_2.display_user_balance()

user_3.deposit(2000)
user_3.withdraw(250)
user_3.withdraw(150)
user_3.withdraw(200)

user_3.display_user_balance()
