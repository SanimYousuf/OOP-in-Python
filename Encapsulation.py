# Encapsulation = Hide details using access modifiers

class Bank:
    def __init__(self, name, initialDeposit) -> None:
        self.name = name                # -> public attribute
        self._branch = 'Faridpur'       # -> protected attribute
        self.__balance = initialDeposit # -> private attribute

    def getBalance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Insufficient balance.'

Saikat = Bank("Samiul Saikat", 500)
Saikat.name = 'Shahil'
Saikat._branch = 'Dhaka'
print(Saikat.getBalance())
print(Saikat.name)
print(Saikat._branch)

print(dir(Saikat))
print(Saikat._Bank__balance)