class Shop:
    shoppingMall = "R & F"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []      #cart is an instance attribute

    def addToCart(self, item):
        self.cart.append(item)

customer = Shop('Customer')
customer.addToCart('Face Wash')
customer.addToCart('Facial Cream')
print(customer.cart)

person = Shop('Person')
person.addToCart('GPU')
person.addToCart('SSD')
print(person.cart)
    