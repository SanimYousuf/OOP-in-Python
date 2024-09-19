class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.minWithdraw = 100
        self.maxWithdraw = 100000

    def getBalance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.minWithdraw:
            print(f'You cannot withdraw amount less than {self.minWithdraw}')
        elif amount > self.maxWithdraw:
            print(f'You cannot withdraw amount more than {self.maxWithdraw}')
        else:
            self.balance -= amount
            print(f'You have successfully withdraw amount {amount}')
            print(f'Your balance after withdraw: {self.getBalance()}')
        
IBBL = Bank(10000)
IBBL.withdraw(1500)
print(IBBL.balance)