t=int(input())
while(t):
    t-=1
    s=input()
    s=list(s)
    size=len(s)
    ch=False
    if(s[0]*size==s):
        print("no answer")
    else:
        for i in range(size-2,-1,-1):
            for j in range(size-1,i,-1):
                if(s[i]<s[j]):
                    s[i],s[j]=s[j],s[i]
                    s=s[:i+1]+s[size-1:i:-1]
                    ch=True
                    break
            if ch:
                break
        print(''.join(s))
