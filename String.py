"""
#1
s=str(input("Enter a string : "))
v='AEIOUaeiou'
c=0
for i in s:
    if i in v:
        c=c+1
print("Total no. of vowels in ",s," : ",c)


#2
s=str(input("Enter a string : "))
rs=''
for i in s:
    rs=i+rs
print("Reversed text : ",rs)


#3
s=str(input("Enter a string : "))
rs=''
for i in s:
    rs=i+rs
print("Reversed text : ",rs)
if s==rs:
    print("Palindrome")
else:
    print("Not Palindrome")


#4
s=str(input("Enter a String : "))
cu=0
cl=0
cn=0
sc=0
for i in s:
    if i.isupper():
        cu+=1
    elif i.islower():
        cl+=1
    elif i.isdigit():
        cn+=1
    else:
        sc+=1
print("Upper Case letters in the string : ",cu)
print("Lower Case letters in the string : ",cl)
print("Numbers in the string : ",cn)
print("Special Characters in the string : ",sc)


#5
s=str(input("Enter a String : "))
s=s.replace(" ","_")
print(s)


#6
s=str(input("Enter a String : "))
l=sorted(set(s))
for i in l:
    print(i," : ",s.count(i))


#7
s=str(input("Enter a String : "))
rs="".join(dict.fromkeys(s))
print("Result string after removing duplicate characters : ",rs)


#8
s=str(input("Enter a String : "))
d=dict.fromkeys(s)
print(d)
for i in d:
    if s.count(i)==1:
        print("First non repeating character in the string : ",i)
        break


#9
s1=str(input("Enter String 1 : "))
s1=s1.lower()
s2=str(input("Enter String 2 : "))
s2=s2.lower()
s=set(s1)|set(s2)
c=0
for i in s:
    if i!=" ":
        if s1.count(i)!=s2.count(i):
            c=1
if c==0:
    print("Anagram")
else:
    print("Not an Anagram")
    


#10
s=str(input("Enter a String : "))
nl=[]
l=s.split()
for i in l:
    nl.append(i.capitalize())
ns=" ".join(nl)
print(ns)


#11
s=str(input("Enter a String : "))
l=s.split()
d=dict()
for i in l:
    c=len(i)
    if c not in d:
        d[c]=[]
    d[c].append(i)
m=max(d)
st=" , ".join(d[m])
print("Longest word/words in the string : ",st)


#12
s='aaabbc'
l=list(s)
nl=[]
for i in l:
    if i not in nl:
        nl.append(i)
        nl.append(str(l.count(i)))
print("".join(nl))


#13
s=str(input("Enter a String : "))
w=len(s.split())
c=len(s)
n=0
for i in s:
    if i.isdigit():
        n+=1
print("No. of words in the string : ",w)
print("No. of characters in the string : ",c)
print("No. of digits in the string : ",n)


#14
s=str(input("Enter a String : "))
n=int(input("Enter the no. you want to rotate the string by : "))
n=n%len(s)
ns=s[n:]+s[:n]
print("String after rotation : ",ns)


#15
s=str(input("Enter a String : "))
l=len(s)
ss=[]
for i in range(l):
    for j in range(i+1,l+1):
        ss.append(s[i:j])
print(ss)
"""
