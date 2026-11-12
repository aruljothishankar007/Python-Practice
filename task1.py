'''
#1
name=(input("enter your name"))
print ("welcome",name)

#2
a=input("student name;")
b=input("enter your age:")
c=input("enter your department:")
print("======Student Details======")
print("Student Name:",a)
print("age:",b)
print("deoartment:",c)

#3
laptop=int(input("laptop price:"))
mobile=int(input("mobile price:"))
tab=int(input("tab price:"))
total=laptop+mobile+tab
print("total",total)



#4
km= float(input("enter distance in kilometer km:"))
miles=km * 0.621371
print("distance in miles",miles)


#6
num = int(input("Enter an integer: "))
decimal = float(input("Enter a decimal number: "))
text = input("Enter a string: ")
print("\n===== DATA TYPES =====")
print("Integer:", num, "| Type:", type(num))
print("Decimal:", decimal, "| Type:", type(decimal))
print("String:", text, "| Type:", type(text))


#7
a=int(input("enter first number"))
b=int(input("enter second number"))
print("before swaping")
print("a=a" ,a)
print("b=b",b)
print("after swaping")
print("a=b",b)
print("b=a",a)


#8
a=float(input("enter the principle"))
b=float(input("enter the rate"))
c=float(input("enter the time"))
si=(a*b*c)/100
print("simple interest",si)


#9
a=float(input("tamil mark"))
b=float(input("english mark"))
c=float(input("matha mark"))
d=float(input("science mark"))
e=float(input("social mark"))
total = a + b + c + d + e
average = total / 5
print("total marks",total)
print("average mark",average)


'''

#10
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)





#11
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
else:
    print("Not a positive number")


#12
    num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")






