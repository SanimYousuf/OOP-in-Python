class Vehicle:
    def __init__(self, brand, price) -> None:
        self.brand = brand
        self.price = price

    def __repr__(self) -> str:
        return f'Brand: {self.brand}, Price: {self.price},'

class Bus(Vehicle):
    def __init__(self, brand, price, seat) -> None:
        self.seat = seat
        super().__init__(brand, price)

    def __repr__(self) -> str:
        return super().__repr__() + f' Seat: {self.seat},'

class Car(Vehicle):
    def __init__(self, brand, price, model) -> None:
        self.model = model
        super().__init__(brand, price)

class AC_Bus(Bus):
    def __init__(self, brand, price, seat, origin) -> None:
        self.origin = origin
        super().__init__(brand, price, seat)

    def __repr__(self) -> str:
        return super().__repr__() + f' Origin: {self.origin}.'

Shohagh = AC_Bus('Shohagh Paribahan', '1.9 crore', 27, 'South Korea')
print(Shohagh)