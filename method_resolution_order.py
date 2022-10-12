class Phone:

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class Product:

    def buy(self):
        print("Product buy method")

class SmartPhone(Product,Phone):
    pass

s = SmartPhone(15000,"Samsung",48)

s.buy()

# Method Resolution Order 
