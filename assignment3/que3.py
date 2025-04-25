def growth(cycles):
    total=1
    for i in range(1,cycles+1):
        if (i%2==0):
            total+=1
        else:
            total*=2
    return total
t=int(input())
while(t):
    num=int(input())
    print(growth(num))
    t-=1