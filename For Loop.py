"""
#1
for i in range (1,11):
    print(i)

#2
for i in range(1,21):
    if i%2==0:
        print(i)

#3
n=0
for i in range (11):
    n=n+i
print (n)

#4
n=int(input("Enter a no. : "))
print ("Table of ",n," :")
for i in range(1,11):
    print(n," * ",i," = ",n*i)

#5
st=str(input("Enter a string : "))
c=0
for chr in st:
    c=c+1
print(c," Characters")

#6
for i in range(1,11):
    if i==5:
        break
    print(i)

#7
l=list(input("Enter no. list : ").split())
a=0
for n in l:
    if n=='25':
        a=1
        print("Found")
        break
if a==0:
    print("Not Found")


#8
l=list(input("Enter no. list : ").split())
a=0
for n in l:
    if int(n)<0:
        a=1
        print("First negative no. found : ",n)
        break
if a==0:
    print("No negative no. found")

#9
for i in range(1,11):
    if i==5:
        continue
    print(i)

#10
for i in range(1,21):
    if i%2!=0:
        print(i)

#11
st="PYTHON"
for ch in st:
    if ch!='O':
        print(ch,end="")

#12
for i in range (1,6):
    pass

#13
fir i in range (1,11):
    if i==6:
        pass

#14
l=list(input("Enter no. list : ").split())
a=0
for n in l:
    if n=='100':
        a=1
        print("Found")
        break
else:
    if a==0:
        print("Not Found")

#15
n=int(input("Enter a no. : "))
f=0
for i in range(1,n+1):
    if n%i==0:
        f+=1
if f==2:
    print("Prime")
else:
    print("Not Prime")

#16
for i in range(6):
    for j in range(i):
        print("*",end="")
    print()

#17
for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#18
for i in range(6):
    for j in range(1,i+1):
        print(j,end="")
    print()

#19
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()

#20
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i*2):
        print("*",end="")
    print()

#21
for i in range(6,1,-1):
    for k in range(i,6):
        print(" ",end="")
    for j in range(1,i*2-2):
        print("*",end="")
    print()
"""
