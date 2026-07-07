l=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
li=[1,2,3,4,5,6,7,8,9]
p='X'
fl=1
counter=0
while True:
    print("\n\tTIC-TAC-TOE")
    print(f"\t{li[0]} | {li[1]} | {li[2]}")
    print("\t---------")
    print(f"\t{li[3]} | {li[4]} | {li[5]}")
    print("\t---------")
    print(f"\t{li[6]} | {li[7]} | {li[8]}")
    if fl==0:
        break
    ch=int(input(f"\n\tPlayer {p}'s Turn : "))
    if ch<1 or ch>9:
        print("\n\tInvalid choice")
        continue
    if li[ch-1]=='X' or li[ch-1]=='O':
        print("\tNo Cheating")
        continue
    li[ch-1]=p
    counter+=1
    for a,b,c in l:
        if li[a]==li[b]==li[c]:
            print(f"\n\tPlayer {p} WINS")
            fl=0
    if counter==9 and fl==1:
        print("\n\tMatch TIE")
        fl=0
        continue
    if p=='X':
        p='O'
    else:
        p='X'        
        
