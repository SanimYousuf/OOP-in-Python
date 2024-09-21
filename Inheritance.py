class Device:
    def __init__(self, brand, color, price) -> None:
        self.brand = brand
        self.color = color
        self.price = price

    def run(self):
        return f'Running device: {self.brand}'

class Laptop:
    def __init__(self, memory) -> None:
        self.memory = memory

    def coding(self):
        return f'Learning Python and SQL'
    
class Phone(Device):
    def __init__(self, brand, color, price, slot) -> None:
        self.slot = slot

        super().__init__(brand, color, price)

    def call(self, number):
        return f'Calling to: {number}'
        
    def __repr__(self) -> str:
        return f'Phone brand is: {self.brand}, color: {self.color}, price: {self.price}, Sim slot: {self.slot}'
    

myPhone = Phone('Realme', 'Glossy green', 17500, 2)
print(myPhone)