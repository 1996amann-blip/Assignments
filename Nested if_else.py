"""
#1
a=int(input("Enter first no. : "))
b=int(input("Enter second no. : "))
c=int(input("Enter third no. : "))
if a>b:
    if a>c:
        print(a," is the greatest")
    else:
        print(c," is the greatest")
else:
    if b>a:
        if b>c:
            print(b," is the greatest")
        else:
            print(c," is the greatest")

#2
a=float(input("Enter a no. : "))
if a>0:
    print("Positive no.")
else:
    if a<0:
        print("Negative no.")
    else:
        print("Entered no. is Zero")

#3
m=float(input("Enter Marks : "))
if m>=90:
    print("Grade : A")
else:
    if m>=75:
        print("Grade : B")
    else:
        if m>=60:
            print("Grade : C")
        else:
            print ("Fail")

#4
print("Enter the length of all 3 sides in a Triangle : ")
a=float(input("Side A : "))
b=float(input("Side B : "))
c=float(input("Side C : "))
if a==b:
    if a==c:
        print("Equilateral Triangle")
    else:
        print("Isosceles Triangle")
else:
    if a==c:
        print("Isosceles Triangle")
    else:
        if b==c:
            print("Isosceles Triangle")
        else:
            print("Scalene Triangle")

#5
ch=input("Enter a Character : ")
if len(ch)==1:
    if ch>='A' and ch<='Z':
        print("Uppercase Character")
    else:
        if ch>='a' and ch<='z':
            print("Lowercase Character")
        else:
            if ch>='0' and ch<='9':
                print("Digit")
            else:
                print("Special Character")
else:
    print("More than 1 character entered")

#6
u=int(input("Enter the units of electricity used : "))
if u>=0:
    if u<=50:
        print("Electricity Bill : ",(u*3.5))
    else:
        if u<=200:
            print("Electricity Bill : ",(u*4.5))
        else:
            if u<=250:
                print("Electricity Bill : ",(u*5.8))
            else:
                print("Electricity Bill : ",(u*6.3))

#7
u=input("Enter Username : ")
p=input("Enter Password : ")
if u=='1996aman':
    if p=='admin123':
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Incorrect Username")

#8
a=float(input("Enter marks in Maths : "))
b=float(input("Enter marks in Physics : "))
c=float(input("Enter marks in Chemistry : "))
if a>=40 and b>=40 and c>=40:
    print("Pass with",(a+b+c)/3,"%")
else:
    if a<40:
        print("Fail in Maths")
    if b<40:
        print("Fail in Physics")
    if c<40:
        print("Fail in Chemistry")

#9
a=int(input("Enter no.1 : "))
b=int(input("Enter no.2 : "))
c=int(input("Enter no.3 : "))
if a>b:
    if a>c:
        if b>c:
            print(b,"is the second greatest no.")
        else:
            print(c,"is the second greatest no.")
    else:
        print(a,"is the second greatest no.")
else:
    if b>c:
        if a>c:
            print(a,"is the second greatest no.")
        else:
            print(c,"is the second greatest no.")
    else:
        print(b,"is the second greatest no.")
        
#10
a=int(input("Enter Age : "))
if a>=18 and a<=60:
    s=float(input("Enter Salary : "))
    if s>=15000:
        cs=int(input("Enter Credit Score : "))
        if cs>=700:
            print("Eligible for loan")
        else:
            print("Credit Score below required for loan")
    else:
        print("Salary below required for loan")
else:
    print("Age does not match eligibilty criteria for loan")
"""
