"""
#LAMBDA

#1a

add=lambda a,b:a+b
a=int(input("Enter 1st no. : "))
b=int(input("Enter 2nd no. : "))
print("Result : ",add(a,b))


#1b

checkEven=lambda num:'Even' if num%2==0 else 'Odd'
n=int(input("Enter a no. : "))
print(f"{n} is {checkEven(n)}")



#MAP

#2a

square=lambda num:num**2
li=[1,2,3,4,5,6,7,8,9,10]
print("Given List : ",li)
s=list(map(square,li))
print("Result : ",s)

#2b

up=lambda st:st.upper()
li=['aman','rahul','mohan','jeet']
print("Given list : ",li)
rl=list(map(up,li))
print("Result : ",rl)



#FILTER

#3a

findEven=lambda num:num%2==0
li=[2,3,9,44,8,26,45,7]
print("Given List : ",li)
rl=list(filter(findEven,li))
print("Result : ",rl)

#3b

findlen=lambda st:len(st)>5
li=['Maneesh','Aman','Shubham','Manveer','Ramkumar','Raj']
print("Given list : ",li)
rl=list(filter(findlen,li))
print("Result : ",rl)



#REDUCE

#4a

from functools import reduce
Sum=lambda a,b:a+b
li=[43,45,2,67,5]
print("Given List : ",li)
res=reduce(Sum,li)
print("Result : ",res)

#4b

from functools import reduce
mul=lambda a,b:a*b
li=[1,2,3,4,5]
print("Given list : ",li)
res=reduce(mul,li)
print("Result : ",res)



#LAMBDA + MAP

#5

xten=lambda num: num*10
li=[46,97,6,8,46]
print("Given list : ",li)
rl=list(map(xten,li))
print("Result : ",rl)



#LAMBDA + FILTER

#6

divthree=lambda num:num%3==0
li=[36,64,99,56,27,65,90,33]
print("Given list : ",li)
rl=list(filter(divthree,li))
print("Result : ",rl)



#7

from functools import reduce
maximum=lambda a,b:max(a,b)
li=[23,45,82,90,37,4]
print("Given List : ",li)
res=reduce(maximum,li)
print("Result : ",res)



#8

Cap=lambda st:st.capitalize()
li=['rahul','aman','raj','rishi']
print("Given list : ",li)
res=list(map(Cap,li))
print("Result : ",res)



#9

pal=lambda st:st==st[::-1]
li=['aman','bob','john','neven','otto']
print("Given list : ",li)
res=list(filter(pal,li))
print("Result : ",res)

"""
