class Phone:
    manufactured = 'China'

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def sendSMS(self, phone, sms):
        text = f'Sending to: {phone} {sms}'
        print(text)

myPhone = Phone('Sanim', 'Samsung', 16000)
print(myPhone.owner, myPhone.brand, myPhone.price)

myPhone.sendSMS('iPhone 6', 'Hi there!')   