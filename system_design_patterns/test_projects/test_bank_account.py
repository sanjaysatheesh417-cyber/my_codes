
from system_design_patterns.projects.bank_account import BankAccount

acc=BankAccount("sanjay",10000,18,"Axis")
acc.withdraw(1000)
acc.check_balance()
acc.deposit(5000)
acc.transfer(5000,"IDBI")