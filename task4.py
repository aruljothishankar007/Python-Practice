'''
#6
a=(10,20,30)
b=(40,50,60)
result=a+b
print(" concatenate tuple",result)
print(type(result))


#1
def listt():
    a = []
    n = int(input("Enter how many numbers: "))
    i = 1
    while i < n:
        s = int(input("Enter number: "))
        a.append(s)
        i += 1
    print("a",a)
listt()

'''
'''
#13
def greet():
    a=input("Enter a employee ID:")
    b=input("Enter a employee name:")
    c=input("Enter a employee designation:")
    d=input("Enter a employee salary:")
    print(f"employee ID:{a}  employee name:{b}  employee designation:{c} employee salary")
greet()    
'''

'''
#15
def listt():
    a = {"apple": 100,"mango": 80,"orange": 60,"banana": 50,"grapes": 90}
    name = input("Enter product name: ")
    print("Price:", a.get(name, "Product not found"))
listt()
'''

#11
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print("Symmetric Difference:", c)

#8
a = {10, 20, 30}
b = {30, 40, 50}
c = a.union(b)
print("Union:", c)


#9
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print("Intersection:", c)












