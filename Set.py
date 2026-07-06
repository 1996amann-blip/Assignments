"""
#1
s=set()
n=int(input("Enter the no. of elements you want to add : "))
for i in range(n):
    e=input(f"Enter element {i+1} : ")
    s.add(e)
print("Set after adding the elements : ", s)


#2
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("Set 1 :",s1)
print("Set 2 :",s2)

print("Union of Sets : ",s1|s2)
print("Intersection of Sets : ",s1&s2)


#3
l=[1,2,2,5,2,1,5,3,2]
print("Original list : ",l)
nl=list(set(l))
print("New list : ",nl)


#4
s={'a',1,34,'am',3.45}
k=1
print("Set : ",s)
c=input("Enter the element you want to check : ")
for i in s:
    if type(i)==int:
        i=str(i)
    if i==c:
        print(c," Exist's in the set")
        k=0
        break
if k==1:
    print(c," Does not exist in the set")


#5
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("Set 1 :",s1)
print("Set 2 :",s2)
print("Different elements in Set 1 : ",s1-s2)
print("Different elements in Set 2 : ",s2-s1)
print("Different elements in both Sets : ",s1^s2)


#6
l1=[1,3,5,3,6,1,3,2,4,5]
print("List 1 : ",l1)
l2=[6,4,5,3,8,5,3]
print("List 2 : ",l2)
s1=set(l1)
s2=set(l2)
print("Common elements in the lists : ",s1&s2)


#7
s1={1,2,3,4,5,6,7,8,9,10}
s2={2,5,7,8,78}
print("Set 1 :",s1)
print("Set 2 :",s2)
c=1
for i in s2:
    if i not in s1:
        c=0
        print("Set 2 not a subset of Set 1")
        break
if c==1:
    print("Set 2 is a subset of Set 1")


#8
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("Set 1 :",s1)
print("Set 2 :",s2)
print("Symmetric Difference betwwen both Sets : ",s1^s2)


#9
l=[1,3,'a',3,'g',4,'g']
print("List : ",l)
s=set(l)
print("Unique elements in the List : ",s)


#10
s1={1,2,3,4,5}
s2={3,4,5,6,7}
print("Set 1 :",s1)
print("Set 2 :",s2)
print("Set 1 after removing common elements : ",s1-s2)
print("Set 2 after removing common elements : ",s2-s1)


#11
s=set()
n=int(input("Enter the no. of elements you want to add : "))
for i in range(n):
    e=int(input(f"Enter element {i+1} : "))
    s.add(e)
print("Set after adding the elements : ", s)

m=max(s)
print("Missing no. between 1 to ",m," :")
for j in range(1,m):
    if j not in s:
        print(j)


#12
s1={1,2,3,4,5}
s2={6,7}
s=set()
print("Set 1 :",s1)
print("Set 2 :",s2)
if s1&s2==s:
    print("No common elements found")
else:
    print("Common elements : ",s2&s1)


#13
s={"Aman","Rahul","Vivek","Mohit"}
print("Set of strings : ",s)
ns=set()
for st in s:
    st=st.upper()
    ns.add(st)
print("Updated set of strings : ",ns)


#14
s=str(input("Enter a string : "))
print("Vowels in string",s," : ",end="")
cs=set()
s=s.upper()
for c in s:
    cs.add(c)
v='AEIOU'

for i in cs:
    if i in v:
        print(i," ",end="")


#15
l=[1,3,4,3,5,6,5,4,8,9]
s=set(l)
print("List : ",l)
print("Elemnts that appear only once in the list : ")
for i in s:
    if l.count(i)==1:
        print(i)
"""
