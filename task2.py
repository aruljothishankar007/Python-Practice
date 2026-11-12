'''
a=int(input("Enter your number:"))
if a>0:
     print("positive number")
if a<0:
     print("negative number")
else:
     print("zero")
 

tamil=int(input("Enter your tamil mark"))
english=int(input("Enter your english mark"))
maths=int(input("Enter your maths mark"))
science=int(input("Enter your science mark"))
social=int(input("Enter your social mark"))
total=tamil+english+maths+science+social
average=total/5
print("total mark:", total)
print(" average  mark:",average)


a=int(input("enter your number:"))
if a%5==0:
     print("divisible by 5")
else:
     print("not divisible by 5")

a=int(input("enter your number:"))
if a%2==0:
     print("even number")
else:
     print("odd number")



a=int(input("Enter your number:"))
if a>=90 and mark<=100:
     print("Grade A")
elif a>=80:
     print(" grade B")
elif a>=70:
     print("grade C")
elif a>=50:
     print("grade D")
elif a>=0:
     print("FAIL")
else:
     print()
'''



'''
a=int(input("Enter your age:"))
if a>=18:
     print("eligible")
else:
     print("not eligible")

'''



a=int(input("Enter your number"))
t=a
b=0 
while a>0:
     e=a%10
     b=(b*10)+e
     a=a//10
if t==b:
     print("palindrome")
else:
     print(" not a palindrome")



n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print()
'''
a=int(input("enter your number"))
for i in range(1,a+1):
     if i%3==0:
          continue
     print(i)




a=int(input("enter your message"))
if "aeiou":
     print("it is vowel")
else:
     print("it is not a vowel")

'''


a=int(input("enter your number:"))
for i in range(1,11):
     print(f"{i}x{a}={i*a}")




a = input("Enter a string: ")

rev = ""

for i in a:
    rev = i + rev

print("Reversed string:", rev)



   
   
