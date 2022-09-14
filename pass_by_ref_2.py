'''
class Customer:

    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))

cust = Customer('Ravi')
print(id(cust))

greet(cust)

'''

class Customer:

    def __init__(self,name):
        self.name = name

def greet(customer):
    print(id(customer))
    customer.name = 'Rafa'
    print(customer.name)
    print(id(customer))

cust = Customer('Ravi')
print(id(cust))

greet(cust)

print(cust.name)

# Objects of a class are mutable like lists,dict and sets
