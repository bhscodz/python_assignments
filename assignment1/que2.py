import random
max_num=100
z=random.randint(0,max_num)
rand_list=[0]*z+[1]*(max_num-z)

random.shuffle(rand_list)
print(rand_list)
max_length=0
temp=0
for i in rand_list:
    if i==1:
        temp=0
    else:
        temp+=1
        max_length=max(max_length,temp)
print(max_length)