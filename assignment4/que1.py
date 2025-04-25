#love letter mystery
t=int(input("t"))
while(t):
    b=input()
    b=list(b)
    count=0
    size=len(b)
    for i in range(0,size//2,1):
        while(b[i]!=b[size-1-i]):
            ch=b[size-1-i]
            if ch>='a':
                b[size-1-i]=chr(ord(ch)-1)
                count+=1
            else :
                print("pallindrom not possible")
    print(count)
    t-=1