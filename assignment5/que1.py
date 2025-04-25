l,r=int(input("enter l")),int(input("enter r"))
max_num=0
for i in range(l,r+1):
    for j in range(i,r+1):
        max_num=max((i^j),max_num)
print(max_num)