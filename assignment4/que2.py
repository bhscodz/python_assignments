import math
t=int(input())
while(t):
    t-=1
    count=0
    num1,num2=tuple(map(int,list(input().strip().split())))
    for i in range(num1,num2+1):
        if(math.isqrt(i)**2==i):
            count+=1
    print(count)