#Lists: Cloning required because the operations will change original list
'''
def change(L):
    print(id(L))
    L.append(5)
    print(id(L))

L1 = [1,2,3,4]
print(L1)
print(id(L1))

#change(L1)
change(L1[:]) #cloning

print(L1)
'''

#Tuples: Cloning not required since tuples are immutable

def change(L):
    print(id(L))
    L = L + (5,6)
    print(id(L))

L1 = (1,2,3,4)
print(L1)
print(id(L1))

change(L1)

print(L1)
