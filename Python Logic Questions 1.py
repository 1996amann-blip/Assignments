"""
#!
i=float(input("Enter annual income : "))
d=float(input("Enter annual deductables : "))
gi=i-d
if gi>=2400000:
    print("Income Tax : ",gi*0.30)
elif gi>=2000000:
    print("Income Tax : ",gi*0.25)
elif gi>=1600000:
    print("Income Tax : ",gi*0.20)
elif gi>=1200000:
    print("Income Tax : ",gi*0.15)
elif gi>=800000:
    print("Income Tax : ",gi*0.10)
elif gi>=400000:
    print("Income Tax : ",gi*0.50)
else:
    print("Income Tax : 0")

#2
amt=float(input("Enter initial Balance : "))
i=int(input("""#1 Balance Check
#2 Withdraw
"""))
if i==1:
    print("Available Balance : ",amt)
elif i==2:
    wa=float(input("Enter Withdrawal Amount : "))
    if wa<=amt:
        amt=amt-wa
        print("Available Balance : ",amt)
    else:
        print("Insufficient Balance")
else:
    print("Choice Invalid")

#3
e=int(input("Experience (in years) : "))
p=int(input("""#Performance Grade
#1 Poor
#2 Below Average
#3 Average
#4 Good
#5 Excellent
"""))
if e>=3 and p==5:
    print("Recommended for Promotion")
elif e>=5 and p>=4:
    print("Eligible for Promotion")
elif e>=3 and p>=3:
    print("Eligible for Promotion")
elif e<3:
    print("Not Eligible for Promotion")
elif p>5:
    print("Invalid Performance Grade")
else:
    print("Not Eligible for Promotion")

#4
print("Enter Marks")
m=float(input("Maths : "))
p=float(input("Physics : "))
c=float(input("Chemistry : "))
e=float(input("English : "))
avg=(m+p+c+e)/4
if avg<50:
    print("Grade : F")
else:
    if avg>=90 and avg<=100:
        print("Grade : A")
    else:
        if avg>=75 and avg<90:
            print("Grade : B")
        else:
            if avg>=65 and avg<75:
                print("Grade : C")
            else:
                if avg>=50 and avg<65:
                    print("Grade : D")
                else:
                    if avg<50:
                        print("Grade : F")
                    else:
                        print("Invalid Entry")

#5
p=input("Enter Password : ")
u=set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
l=set("abcdefghijklmnopqrstuvwxyz")
n=set("0123456789")
s=set("""~!@#$%^&*()-_=+[]{}|;:'",.<>/?""")
P=set(p)
if len(p)>=8:
    if (P & u) and (P & l) and (P & s) and (P & n):
        print("Strong Password")
    else:
        print("Weak Password")
else:
    print("Weak Password")

#6
amt=float(input("Enter Order Amount : "))
l=input("""#Enter Location
#A
#B
#C
#D
""")
if (l=='A' or l=='a') and amt>=200:
    print("Delivery Charge : 0")
elif (l=='A' or l=='a') and amt<200:
    print("Delivery Charge : ",amt*0.02)
elif (l=='B' or l=='b') and amt>=500:
    print("Delivery Charge : 0")
elif (l=='B' or l=='b') and amt<500:
    print("Delivery Charge : ",amt*0.05)
elif (l=='C' or l=='c') and amt>=700:
    print("Delivery Charge : 0")
elif (l=='C' or l=='c') and amt<700:
    print("Delivery Charge : ",amt*0.1)
elif (l=='D' or l=='d') and amt>=1200:
    print("Delivery Charge : 0")
elif (l=='D' or l=='d') and amt<1200:
    print("Delivery Charge : ",amt*0.15)
else:
    print("Delivery not available")
   
#7
print("Enter details for Online Exam Qualification Check : ")
age=int(input("Age : "))

if age<18 and:
    print("Age below Eligibility Criteria")
else:
    edu=int(input ("Select Highest Educational Qualification : \n1 High School or Below \n2 Under Graduate or above \n1 or 2 : "))
    if edu==1:
        print("Educational Qualification below Eligibility Criteria")
    elif edu==2:
        i=input("Identification Provided (Y/N) : ")
        if i=='N' or i=='n':
            print("Identification Required")
        elif i=='Y' or i=='y':
            f=input("Fees Submitted (Y/N) : ")
            if f=='N' or f=='n':
                print("Submit Fees")
            elif f=='Y' or f=='y':
                print("Qualified for Online Exam")
            else:
                print("Invalid Choice")
        else:
            print("Invalid Choice")
    else:
        if edu!=1 or edu!=2:
            print("Invalid Choice")

#8
age=int(input("Enter Age : "))
t=int(input("Select Movie Timing:\n1 8:00 AM\n2 8:30 AM\n3 10:00 AM\n4 11:30 AM\n5 1:00 PM\n6 2:30PM\n7 4:00 PM\n8 5:30 PM\n9 7:00 PM\n10 9:30PM\nSelect (1-10) : "))
if age>=18:
    if t==1 or t==2:
        print("Ticket Price : ",150-(150*0.1))
    elif t>=3 and t<=8:
        print("Ticket Price : ",150+(150*0.15))
    elif t>8 and t<=10:
        print("Ticket Price : 150")
    else:
        print("Invalid Choice")
elif age<18 and age>=10:
    if t==1 or t==2:
        print("Ticket Price : ",150-(150*0.1)+(150*0.05))
    elif t>=3 and t<=8:
        print("Ticket Price : ",150+(150*0.15)-(150*0.05))
    elif t>8 and t<=10:
        print("Ticket Price : ",150-(150*0.05))
    else:
        print("Invalid Choice")
elif age<10 and age>=6:
    if t==1 or t==2:
        print("Ticket Price : ",150-(150*0.1)+(150*0.1))
    elif t>=3 and t<=8:
        print("Ticket Price : ",150+(150*0.15)-(150*0.1))
    elif t>8 and t<=10:
        print("Ticket Price : ",150-(150*0.1))
    else:
        print("Invalid Choice")
elif age<6:
    if t>=1 and t<=10:
        print("Free Ticket")
    else:
        print("Invalid Choice")

#9
bal=float(input("Enter Account Balance : "))
if bal>=1500000:
    print("Wealth/Private Account")
elif bal>=100000 and bal<1500000:
    print("Premium Account")
elif bal>=5000 and bal<100000:
    print("Regular Savings Account")
elif bal>=0 and bal<5000:
    print("Student/Basic Savings Account")
else:
    print("Insufficient Balance")

#10
a=float(input("Enter first no. : "))
b=float(input("Enter Second no. : "))
c=int(input("1 Add\n2 Substract\n3 Multiply\n4 Divide\n(1-4) : "))
if c==1:
    print("Result", a+b)
elif c==2:
    print("Result", a-b)
elif c==3:
    print("Result", a*b)
elif c==4:
    print("Result", a/b)
else:
    print("Invalid Choice")
"""
