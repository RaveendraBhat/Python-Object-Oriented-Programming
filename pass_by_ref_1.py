class Customer:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == 'Male':
        print('Hello',customer.name,'sir')
    else:
        print('Hello',customer.name,'madam')

    cust2 = Customer('Rafa','Male')

    return cust2

cust = Customer('Iga','Female')

new_cust = greet(cust)
print(new_cust.name)


