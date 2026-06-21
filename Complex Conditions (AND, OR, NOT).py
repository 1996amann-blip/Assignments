"""
#1
n=int(input("Enter a no. : "))
if n%5==0 and n%11==0:
    print(n," is divisible by 5 & 11")
else:
    print(n," is not divisible by 5 & 11")

#2
a=int(input("Enter Age : "))
s=float(input("Enter Salary : "))
cs=int(input("Enter Credit Score : "))
if a>=21 and s>=25000 and cs>=700:
    print("Eligible for loan")
else:
    if a<21:
        print("Age below eligibility Criteria")
    if s<25000:
        print("Salary below eligibility Criteria")
    if cs<700:
        print("Credit Score below eligibility Criteria")

#3
u=input("Enter Username : ")
p=input("Enter Password : ")
if u=='1996aman' and p=='admin123':
    print("Login Successful")
else:
    print("Login Invalid")

#4
print("Enter Marks")
m=float(input("Maths : "))
p=float(input("Physics : "))
c=float(input("Chemistry : "))
e=float(input("English : "))
avg=(m+p+c+e)/4
if m>=40 and p>=40 and c>=40 and e>=40 and avg>=50:
    print("PASS")
else:
    if m<40:
        print("Fail in Maths")
    if p<40:
        print("Fail in Physics")
    if c<40:
        print("Fail in Chemistry")
    if e<40:
        print("Fail in English")
    if avg<50:
        print("Avg below 50")

#5
n=int(input("Enter a no. : "))
if n>10 and n<100:
    print(n," is between 10 & 100")
else:
    if n==10:
        print("Entered no. is 10")
    if n==100:
        print("Entered no. is 100")
    if n<10 or n>100:
        print(n," is not between 10 & 100")

#6
a=float(input("Enter attendance percentage : "))
m=input("Medical Certificate available (Y/N) : ")
if a>=75 or m=='Y' or m=='y':
    print("Eligible for exam")
else:
    if a<75 and (m=='n' or m=='N'):
        print("Not Eligible for exam")

#7
print("Enter the date : ")
d=int(input("Day : "))
m=int(input("Month : "))
y=int(input("Year : "))
if (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>=1 and d<=31 and y>=1582:
    print("Valid Date")
elif (m==4 or m==6 or m==9 or m==11) and  d>=1 and d<=30 and y>=1582:
    print("Valid Date")
elif m==2 and (y%400==0 or (y%4==0 and y%100!=0)) and d>=1 and d<=29 and y>=1582:
    print("Valid Date")
elif m==2 and y>=1582 and d>=1 and d<=28:
    print("Valid Date")
else:
    print("Invalid Date")

#8 (Doubt)
E=input("Enter Email ID : ")
if (' 'not in E) and ('@' in E) and ('.com' in E or '.org' in E or '.in' in E):
    print("Valid Email ID")
else:
    print("Invalid Email ID")

#9
a=int(input("Enter age : "))
hs=int(input("""#Select Health Status :
#1 Bad
#2 Below Average
#3 Average
#4 Good
#5 Excellent
"""))
i=float(input("Enter Income : "))
if a>=18 and hs>=3 and hs<6 and i>=15000:
    print("Eligible for Insurance")
elif a>=18 and hs>0 and hs<=2 and i>15000:
    print("Not Eligible for Insurance (Apply again in 1 year)")
else:
    print("Not Eligible")

#10
y=int(input("Enter the Year : "))
if ((y%4==0 and y%100!=0) or y%400==0) and y>=1582:
    print("Leap Year")
elif y>=1582:
    print("Not Leap Year")
else:
    print("Invalid Year")
"""
