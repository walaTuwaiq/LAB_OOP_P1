
from select import select


class Bank:
    def __init__(self,accountNumber, owner, balance):
        self.accountNumber = accountNumber
        self.owner = owner
        self.balance = balance
    
    def Deposit(self,money):
        self.balance += money
        return self.balance

    def Withdrawal(self,money):
        if self.balance >= money:
            self.balance -= money
            return self.balance
        else:
            return "Not enough money!"
        
    def bankFees(self) :
        self.balance = self.balance * 0.93
        return self.balance
        
    def display(self):
        return f"Hello {self.owner}, Your account number is: {self.accountNumber}, And you have {self.balance}SR."


client1 = Bank(3456789,"Ahmed",3000)
print(client1.Withdrawal(100),"Withdrawal Method")
print(client1.Deposit(200),"Deposit Method")
print(client1.bankFees(),"bankFees Method")
print(client1.display(),"display Method")
