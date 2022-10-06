class Product:

    def review(self):
        print("Product customer review")

class Phone(Product):

    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

s = SmartPhone(15000,"Samsung",48)
p = Phone(100000,"Apple",12)

s.buy()
s.review()
p.review()
