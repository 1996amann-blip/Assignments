"""
#23
t=(1,0.45,9+4j,'aman')
print(t)


#24
t=(1,'s',34,5.4,34,6,8j)
print("Tuple length : ",len(t))


#25
t=(2,455,5.7,46,34,67)
print("Max no. in Tuple : ",max(t))
print("Min no. in Tuple : ",min(t))


#26
t=(2,455,5.7,46,34,67)
print(type(t))
t=list([t])
print(type(t))


#27
t=(2,455,5.7,46,34,67)
print("Tuple : ",t)
n=float(input("Enter a no. : "))
if n in t:
    print(n," Exist's in the Tuple")
else:
    print(n," Does not exist in the Tuple")


#28
t=(1,4,7,5,3,2,1,5,7,7,4,3,8)
n=int(input("Enter a no. : "))
print(n," occurs",t.count(n)," times")


#29
t=(23,45,8,74,78,82,9,4,56)
print("Sliced Tuple : ",t[2:6])


#30
t=(1,3,4,2,6,4,2,7,2,4,8)
t1=[]
for i in t:
    if i not in t1:
        t1.append(i)
print("Repeated elements in tuple : ")
for j in t1:
    if t.count(j)>1:
        print(j,"  ",end="")


#31
t1=(1,3,5,7,9)
print("List 1 : ",t1)
t2=(2,4,6,8,10)
print("List 2 : ",t2)
mt=t1+t2
print("Merged List : ",mt)


#32
t=('Aman','Noida',30)
Name,Location,Age=t
print("Name : ",Name)
print("Location : ",Location)
print("Age : ",Age)


#33
t=(2,7,4,2,6,3,1)
st=tuple(sorted(t))
print("Original tuple : ",t)
print("Sorted tuple : ",st)


#34
l=[(1,2,3),('A','B','C')]
d=dict(zip(l[0],l[1]))
print(d)


#35
t=(23,54,77,89,97)
print("Tuple : ",t)
n=int(input("Enter a no. from the tuple : "))
if n not in t:
    print("Element not in Tuple")
else:
    print("Index of ",n," : ",t.index(n))


#36
t=(11,22,33,44,55,66,77)
l=list(t)
print("Original Tuple : ",t)
n=int(input("Enter the element yo want to remove : "))
l.remove(n)
nt=tuple(l)
print("New Tuple : ",nt)


#37
t1=(1,2,3,4,5)
print("Tuple 1 : ",t1)
t2=(3,4,5,6,7)
print("Tuple 2 : ",t2)
ct=tuple(set(t1) & set(t2))
print(ct)


#38
t=(1,2,3,4,5,4,3,2,1)
print("Tuple : ",t)
l=len(t)
k=-1
c=1
for i in range(l-1):
    if t[i]!=t[k]:
        c=0
        print("Not Palindrome")
        break
    else:
        k=k-1
if c==1:
    print("Palindrome")


#39
t=(1,2,4,3,5,2,3,1,4,3,2,1,1,2)
print("Tuple : ",t)
s=set(t)
l=[]
for i in s:
    l.append(t.count(i))

m=max(l)
print("Elements with maximum frequency of ",m," : ",end="")
for j in s:
    if t.count(j)==m:
        print(" ",j,end="")



#40
t=(('Rohit','Vivek','Ajit'),(20,23,43))
n,a=t
if len(n)>=len(a):
    m=len(n)
else:
    m=len(a)
for i in range(m):
    #if n[i]==False:
     #   print("Name : N/A Age : ",a[i])
    #elif a[i]==False:
     #   print("Name : ",n[i]," Age : N/A")
    #else:
        print("Name : ",n[i]," Age : ",a[i])
"""

