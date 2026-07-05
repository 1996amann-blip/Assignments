"""
#BASIC LEVEL
#1
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)


#2
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
print("Sum of all elements in the list : ",sum(l))
print("Average of all elements in the list : ",(sum(l))/(len(l)))


#3
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
print("Largest element in the list : ",max(l))
print("Smallest element in the list : ",min(l))


#4
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
c=0
for x in l:
    c=c+1
print("Total no. of elemnts in the list : ",c)


#5
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
print("\nEntered list in reverse: ",l[::-1])


#6
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)

e=int(input("Enter the element you want to check : "))
if e in l:
    print(e," is in the list")
else:
    print(e," is not in the list")


#7
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
l1=list()
for i in l:
    if i not in l1:
        l1.append(i)
print("Final list : ",l1)


#8
l=list()
n=int(input("Enter the no. of elements in the list : "))
for i in range(n):
    e=int(input(f"Element {i+1} : "))
    l.append(e)

print("\nEntered list : ",l)
l.sort()
print("Ascending order : ",l)
l.reverse()
print("Descending order : ",l)


#9
l1=[1,2,4,5,7]
print("List 1 : ",l1)
l2=[3,5,6,1,8]
print("List 2 : ",l2)
lm=list()
lm=l1
for i in l2:
    if i not in lm:
        lm.append(i)
print("Merged List : ",lm)


#10
l1=[1,2,4,5,7]
print("List 1 : ",l1)
l2=[3,5,6,1,8]
print("List 2 : ",l2)
cl=list()

for i in l1:
    if i in l2:
        cl.append(i)
print("Common List : ",cl)


#11
l=[1,22,43,51,75,66,42,5,22,23,100]
print("List : ",l)
el=list()
ol=list()
for i in l:
    if i%2==0:
        el.append(i)
    else:
        ol.append(i)
print("Even elements : ",el)
print("Odd elements : ",ol)


#12(Doubt)

#13
l=[23,76.39,9,82,90]
print("List : ",l)
l.sort()
ln=len(l)
print(ln)
print("Second largest no. : ",l[ln-2])


#14(Doubt)
l=[1,2,[3,5],6,[8,56,34]]
fl=[]
for sublist in l for item in sublist:
    fl.append(item)
print(fl)


#15
l=[1,9,5,3,7,4,9,5,1,1,2]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)

for j in l1:
    print("Frequency of ",j," in list : ",l.count(j))


#16
l=[1,-34,25,-7,44,5,-5.6]
print("Original List : ",l)
for i in l:
    if i<0:
        ind=l.index(i)
        l[ind]=0
print("Updated List : ",l)


#17
l=[1,9,5,3,7,4,9,5,1,1,2,8,9,2]
print("Original list : ",l)
n=int(input("Enter the no. you want to remove from the list : "))
while n in l:
    l.remove(n)
print("Updated List : ",l)


#18
l=[1,2,3,4,5,5,4,3,2,1]
print(l)
c=1
for i in range(len(l)-1):
    if l[i]!=l[-i-1]:
        c=0
        print("Not Palindrome")
        break
    
if c==1:
    print("Palindrome")


#19
l=[4,5,6,8,10,12,13,15,18,19,20]
print("Original list : ",l)
ma=max(l)
mi=min(l)
print("Missing Consicutive no. : ",end="")
for i in range(mi,ma+1):
    if i not in l:
        print(" ",i, end="")


#20
l1=[5,4,6,23,78,10,8,42]
l2=[5,3,67,5,63,11]
l3=[]
print("List 1 : ",l1)
print("List 2 : ",l2)
ln1=len(l1)
ln2=len(l2)
if ln1>=ln2:
    l3=l1
    c=ln2
else:
    l3=l2
    c=ln1
for i in range(c):
    l3[i]=(l1[i]+l2[i])
print("Final list : ",l3)


#21(Doubt)
l=[2,4,6,4,6,7,9,90,2,1,3,5]
ln=len(l)

s=0
c=1
ls(c)=[]
for i in range(ln):
    for j in range(i,ln):
        if l[j]<l[j+1]:
        s=s+1


#22
l = [1, 9, 5, 3, 7, 4, 9, 5, 1, 1, 2,7,7,7,7]
print("Original List : ", l),7

l1 = sorted(list(set(l)), key=l.count, reverse=True)
print("l1 : ",l1)

fl = []
for j in l1:
    print("Frequency of ", j, " in list : ", l.count(j))
    fl.append(j)

print("List based on frequency : ", fl)
"""



