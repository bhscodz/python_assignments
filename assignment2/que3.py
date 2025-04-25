t=int(input())
while(t):
    num=int(input())
    count =0
    for i in str(num):
        if(num%int(i)==0):
            count+=1
    print(count)
    t-=1
