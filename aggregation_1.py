class Customer:
    
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address

class Address:

    def __init__(self,city,pincode,state):
        self.city = city
        self.pincode = pincode
        self.state = state

add = Address('Bengaluru',560066,'Karnataka')
cust = Customer('Ravi','Male',add)

print(cust)
print(cust.address)
print(cust.address.city)
print(cust.address.city,'-',cust.address.pincode,'-',cust.address.state)
