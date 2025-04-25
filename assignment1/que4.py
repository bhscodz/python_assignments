equivalence=[[],[],[],[],[]]
for i in range(1,10000):
    equivalence[i%5].append(i)
u=list(range(1,10000))
union=[]
for i in equivalence:
    union+=i
union.sort()
print(union==u)