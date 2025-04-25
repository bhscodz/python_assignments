import math
list1=[]
coor="xyz"
print("enter x y z for three points")
for i in range(10):
    point=[]
    for j in coor :
        point.append(int(input(f"enter {j}")))
    list1.append(point)
print(list1)

point_list=[]
for i in list1:
    min_distance=0
    point_list.append([i])
    point_list[-1].append(0)
    for j in list1:
        dist=0
        if(i!=j):
            temp=min_distance
            for k in range(3):
                dist+=(i[k]-j[k])**2
            if (min_distance):
                min_distance=min(min_distance,math.sqrt(dist))
            else:
                min_distance=math.sqrt(dist)
            if(min_distance!=temp):
                point_list[-1][1]=j
print(point_list)
            
            

