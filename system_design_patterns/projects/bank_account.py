class Account:
    def __init__(self, name, balance, age, bank ,savings):
        self.name = name
        self.balance = balance
        self.age = age
        self.bank = bank
        self.savings = savings
class SavingsAccount(Account): #subclass for savings account
    def __init__(self, name, balance, age, bank ,savings):
        super().__init__(name,balance,age,bank,savings)
        print(f"congratulations {self.name}, you have successfully created your savings account ")
    def save(self, amount):
        if self.balance >= amount:
            self.savings += amount
            self.balance -= amount
            print(f"savings amount {amount}, you have successfully saved {amount}")
        else:
            print("insufficient balance")
    def transfer_to_checking_account(self, amount):#to transfer your savings
        if self.savings >= amount:
            self.balance += amount
            print(f"You have successfully transferred {amount} to checking account")
        else:
            print("insufficient balance")
    def check_savings(self):#to check savings account balance
        print(f"Your savings is {self.savings}")
class CheckingAccount(Account):#subclass for checking account
    def __init__(self, name, balance, age, bank, savings):
        super().__init__(name,balance,age,bank ,savings)
        print(f"congratulations {self.name}, you have successfully created your checking account ")
    def withdraw(self, amount):#for withdrawing cash
        if self.balance >= amount:
            self.balance -= amount
            print(f"amount {amount} has been withdrawn and {self.balance} is your balance")
        else:
            print("insufficient balance")
    def deposit(self, amount):#for depositing
        self.balance += amount
        print(f"amount {amount} has been deposited and {self.balance} is your balance")
    def check_balance(self):#to check balance
        print(f"Your balance is {self.balance}")
    def transfer(self, amount, to):#to transfer money to another bank
        self.balance -= amount
        print(f"amount {amount} has been transferred to {to} and {self.balance} is your balance")