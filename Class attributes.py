class Shop:
    cart = [] #cart is a class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def addToCart(self, item):
        self.cart.append(item)

sanim = Shop('Green shop')
sanim.addToCart('Chocolate')
sanim.addToCart('Wrapping paper')

print(sanim.cart)

person = Shop('Person')
person.addToCart('GPU')
person.addToCart('SSD')
print(person.cart)