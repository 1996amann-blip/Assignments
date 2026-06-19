"""
#1
d=int(input("Enter day no. : "))
if d==1:
    print("Monday")
elif d==2:
    print("Tuesday")
elif d==3:
    print("Wednesday")
elif d==4:
    print("Thursday")
elif d==5:
    print("Friday")
elif d==6:
    print("Saturday")
elif d==7:
    print("Sunday")
else:
    print("Invalid Input")

#2
m=int(input("Enter month no. : "))
if m==1:
    print("January")
elif m==2:
    print("February")
elif m==3:
    print("March")
elif m==4:
    print("April")
elif m==5:
    print("May")
elif m==6:
    print("June")
elif m==7:
    print("July")
elif m==8:
    print("August")
elif m==9:
    print("September")
elif m==10:
    print("October")
elif m==11:
    print("November")
elif m==12:
    print("December")
else:
    print("Invalid Input")

#3
p=float(input("Enter the percentage : "))
if p>=90:
    print("Grade : A")
elif p>=80:
    print("Grade : B")
elif p>=70:
    print("Grade : C")
elif p>=60:
    print("Grade : D")
elif p<60:
    print("Grade : F")

#4
e=int(input("Enter your years of experience : "))
if e>=9:
    print("15% to 30% Bonus")
elif e>=3:
    print("10% to 15% Bonus")
elif e>=0:
    print("5% to 10% Bonus")

#5
s=input("Enter Traffic Signal colour : ")
if s=='red' or s=='RED' or s=='Red':
    print("STOP")
elif s=='yellow' or s=='YELLOW' or s=='Yellow':
    print("SLOW DOWN and prepare to stop")
elif s=='green' or s=='GREEN' or s=='Green':
    print("GO")

#6
t=int(input("Enter Temprature : "))
if t>=30:
    print("Hot")
elif t>=20:
    print("Warm")
elif t<=10:
    print("Cold")

#7
s=float(input("Enter the salary : "))
if s>=26910:
    print("Highly Skilled Employee")
elif s>=24804:
    print("Skilled Employee")
elif s>=22568:
    print("Semi-Skilled Employee")
elif s>=20358:
    print("Unskilled Employee")
elif s<20358:
    print("Entered salary is below minimum wage")

#8
pa=float(input("Enter total purchase amount : "))
if pa>5000:
    print("25% Discount")
elif pa>2500:
    print("15%-20% Discount")
elif pa>1000:
    print("10% Discount")
elif pa<=1000:
    print("0%-5% Discount")

#9
i=input("Enter a no. : ")
if len(i)==1:
    print("Single digit no.")
elif len(i)==2:
    print("Double digit no.")
else:
    print("Multi digit no.")

#10
r=int(input("Enter performance rating : "))
if r>=9:
    print("Excellent")
elif r>=6:
    print("Good")
elif r>=4:
    print("Average")
elif r<4:
    print("Poor")
"""
