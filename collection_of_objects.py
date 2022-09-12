class Customer:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print('I am',self.name,'and I am',self.age)

c1 = Customer('Rafa',36)
c2 = Customer('Novak',35)
c3 = Customer('Roger',41)

L = [c1,c2,c3]

for i in L:
    print(i.name,i.age)
    
for i in L:
    i.intro()

# we cannot do this for sets since its immutable and the objects are mutable
