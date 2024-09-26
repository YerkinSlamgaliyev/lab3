class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        elif amount > self.balance:
            print("Insufficient balance for withdrawal.\n")
        else:
            print("Withdrawal amount must be positive.\n")

account = Account("Alice", 1000)

account.deposit(500)  
account.deposit(-100) 

account.withdraw(200)  
account.withdraw(2000) 
account.withdraw(-50)  
account.withdraw(1300) 

account.balance
