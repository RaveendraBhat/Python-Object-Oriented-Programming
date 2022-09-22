class Phone:

    def __init__(self,price,brand,camera):
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s = SmartPhone(15000,'Samsung',48)

print(s.brand)
