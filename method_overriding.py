class Phone:

    def __init__(self,price,brand,camera):

        print("Inside phone constructor")

        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")

s = SmartPhone(15000,"Samsung",48)

s.buy()
        
