"""
#1
i=1
while i<11:
    print(i)
    i+=1

#2
i=1
while i<21:
    if i%2==0:
        print(i)
    i+=1

#3
i=1
while i<21:
    if i%2!=0:
        print(i)
    i+=1

#4
i=10
while i>=1:
    print(i)
    i-=1

#5
i=1
while i<11:
    print("5 * ",i," = ",5*i)
    i+=1

#6
i=1
j=0
while i<11:
    j=j+i
    i+=1
print("Total : ",j)

#7
n=int(input("Enter a no. : "))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1

#8
n=int(input("Enter a no. : "))
c=0
if n==0:
    print("No. of digits : 1")
if n<0:
    n=-n
if n>0:
    while n>0:
        n=n//10
        c=c+1
if c>0:
    print ("No. of digits : ",c)

#9
n=int(input("Enter a no. : "))
rn=0
while n>0:
    d=n%10
    rn=rn*10+d
    n=n//10
print("Reversed no. : ",rn)

#10
n=int(input("Enter a no. : "))
on=n
rn=0
while n>0:
    d=n%10
    rn=(rn*10)+d
    n=n//10
print("Reversed no. : ",rn)
if on==rn:
    print("Palindrome")
elif on!=rn:
    print("Not Palindrome")

#11
i=1
while i<6:
    j=1
    while j<=i:
        print("*",end="")
        j+=1
    print()
    i=i+1

#12
i=1
while i<6:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i=i+1

#13
p=input("Enter Password : ")
while p!="admin123":
    p=input("Enter Password : ")
if p=="admin123":
    print("Correct Password")

#14
import random
n=random.randint(1,10)
print("Random no. : ",n," \n")
ch=int(input("Enter your Guess : "))
while ch!=n:
    print("\nWRONG")
    ch=int(input("\nEnter your Guess again : "))
    if ch==n:
        print("\nCORRECT")
        break
        
#15
n=int(input("Enter no. : "))
t=0
while n!=0:
    t=t+n
    n=int(input("Enter no. : "))

print("Total : ",t)

#16
n=int(input("Enter a no. : "))
f1=0
f2=1
f3=0
i=0
print("Fibonacci Series till ",n," terms : ")
print(f1)
while i<n-1:
    f3=f1+f2
    print(f3)
    f1=f2
    f2=f3
    i+=1

#17
n=int(input("Enter a no. : "))

c=0
t=0
an=0
if n==0:
    print("No. of digits : 1")
    c=1
if n<0:
    n=-n
n1=n
on=n
if n>0:
    while n>0:
        n=n//10
        c=c+1
if c>0:
    print ("No. of digits : ",c)
if n1>0:
    while n1>0:
        t=n1%10
        n1=n1//10
        an=an+t**c
if an==on:
    print("Armstrong no. : ",an)
else:
    print("Not an Armstrong no : ",on)

#18
i=1

while i<=50:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    if c==2:
        print(i)
    i+=1
"""
