class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def addToCart(self, item, price, quantity):
        product = {'Item' : item, 'Price' : price, 'Quantity' : quantity}
        self.cart.append(product)

    def removeItem(self, item):
        pass

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            #print(item)
            total += item['Price'] * item['Quantity']
        print('Total price: ', total)
        if amount < total:
            print(f'Please provide {total - amount} more')
        else:
            print(f'Here is your extra {amount - total}')

person1 = Shopping('Random 1')
person1.addToCart('Sugar', 80, 1)
person1.addToCart('Onion', 120, 2)
person1.addToCart('Masala', 100, 3)

print(person1.cart)
person1.checkout(600)