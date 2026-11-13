
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


#2
n = int(input("Enter number of values: "))
a = []
even = 0
odd = 0
for i in range(n):
    num = int(input("Enter number: "))
    a.append(num)
    if num % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even:", even)
print("Odd:", odd)





#3
names = []
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter student name: ")
    names.append(name)
search = input("Enter name to search: ")
if search in names:
    print("Name Found")
else:
    print("Name Not Found")



#4
a = [10, 5, 30, 2, 20]
a.sort()
print(a)
a.sort(reverse=True)
print(a)





#5
a = (10, 20, 5, 30)
big = a[0]
small = a[0]
for n in a:
    if n > big:
        big = n
    if n < small:
        small = n
print("Maximum:", big)
print("Minimum:", small)


#7
name = input("Enter name: ")
roll = input("Enter roll number: ")
dept = input("Enter department: ")
marks = int(input("Enter marks: "))

student = (name, roll, dept, marks)

print("Student Details:", student)
'''
'''
#8
a = {10, 20, 30}
b = {30, 40, 50}
c = a.union(b)
print("Union:",c)


#9
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.intersection(b)
print("Intersection:", c)


#10
a = {1, 2, 3}
b = {3, 4, 5}
print("Difference:", a - b)




#11
a = {10, 20, 30, 40}
b = {30, 40, 50, 60}
c = a.symmetric_difference(b)
print("Symmetric Difference:", c)



#13
def greet():
    a=input("Enter a employee ID:")
    b=input("Enter a employee name:")
    c=input("Enter a employee designation:")
    d=input("Enter a employee salary:")
    print(f"employee ID:{a}  employee name:{b}  employee designation:{c} employee salary{d}")
greet()



#15
def listt():
    a = {"apple": 100,"mango": 80,"orange": 60,"banana": 50,"grapes": 90}
    name = input("Enter product name: ")
    print("Price:", a.get(name, "Product not found"))
listt()

