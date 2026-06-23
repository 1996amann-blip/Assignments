"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(chr(64+i),end="")
    print()


k=1
m=-1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end="")
        k=k+m
        m=-m
    print()


for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(5,0,-1):
    for k in range(i,5):
        if 5-i!=0:
            print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(1,6):
    for k in range(i,5):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
"""
