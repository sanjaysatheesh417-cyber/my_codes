class bank_account:
    def __init__(self, name, balance, age, bank):
        self.name = name
        self.balance = balance
        self.age = age
        self.bank = bank
    def withdraw(self, amount):
        self.balance -= amount
        print(f"amount {amount} has been withdrawn and {self.balance} is your balance")
    def deposit(self, amount):
        self.balance += amount
        print(f"amount {amount} has been deposited and {self.balance} is your balance")
    def check_balance(self):
        print(f"Your balance is {self.balance}")
