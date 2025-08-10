class BankAccount:
    def __init__(self, name, balance, age, bank):
        self.name = name
        self.balance = balance
        self.age = age
        self.bank = bank
        print(f"congratulations {self.name}, you have successfully created your account ")
    def withdraw(self, amount):#for withdrawing cash
        self.balance -= amount
        print(f"amount {amount} has been withdrawn and {self.balance} is your balance")
    def deposit(self, amount):#for depositing
        self.balance += amount
        print(f"amount {amount} has been deposited and {self.balance} is your balance")
    def check_balance(self):#to check balance
        print(f"Your balance is {self.balance}")
    def transfer(self, amount, to):#to transfer money to another bank
        self.balance -= amount
        print(f"amount {amount} has been transferred to {to} and {self.balance} is your balance")
