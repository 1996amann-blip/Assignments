"""
#1
n=int(input("Enter a no. : "))
if n%2==0:
    print("Even no.")
else:
    print("Odd no.")

#2
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
if a>b:
    print(a," is greater than ",b)
else:
    print(b," is greater than ",a)

#3
age=int(input("Enter your age : "))
if age>=18:
    print("Eligible for Driving Licence")
else:
    print("Not Eligible for Driving Licence")

#4
m=float(input("Enter marks : "))
if m>=40:
    print("Pass")
else:
    print("Fail")

#5
n=float(input("Enter a no. : "))
if n>0:
    print("The no. is positive")
else:
    print("The no. is negative")

#6
c=input("Enter a character : ")
v="AEIOUaeiou"
if c in v:
    print("Character is a Vowel")
else:
    print("Character is a Consonant")

#7
y=int(input("Enter the Year : "))
if (y%4==0 and y%100!=0) or (y%400==0):
    print("Leap year")
else:
    print("Not Leap Year")

#8
p=input("Enter the password : ")
if p=='admin123':
    print("Valid password")
else:
    print("Invalid password")

#9
s=float(input("Enter your annual salary : "))
if s>=1275000:
    print("Taxable")
else:
    print("Not Taxable")

#10
n=float(input("Enter a number : "))
if n>50:
    print(n," is greater than 50")
else:
    print(n," is not greater than 50")
"""
