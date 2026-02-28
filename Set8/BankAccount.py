#Create Bank Account class with depoist and withdraw
class BankAccount:
    def __init__(self,accno,accholdername):
        self.accno=accno
        self.accholdername=accholdername
        self.balanceAmount=0.0
    def check_balance(self):
        return self.balanceAmount
    def deposit(self,depositAmt):
        self.balanceAmount+=depositAmt
    def withdraw(self,withdrawAmt):
        self.balanceAmount-=withdrawAmt
b1=BankAccount(1,'Lakshmi')
b2=BankAccount(2,'X')
b1.deposit(10000)
b2.deposit(50000)
print(f"Balance in {b1.accholdername} is: {b1.check_balance()}")
print(f"Balance in {b2.accholdername} is: {b2.check_balance()}")

b1.withdraw(1000)
b2.withdraw(2000)
print(f"Balance in {b1.accholdername} is: {b1.check_balance()}")
print(f"Balance in {b2.accholdername} is: {b2.check_balance()}")