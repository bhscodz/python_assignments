print("enter the name of 10 students")
std_list=[]
for i in range(10):
    std_list.append(input(f"enter the name of student {i+1}"))
    if len(std_list[-1])>15:
        std_list[-1]=std_list[-1][:16]
print("names of students")
for i in std_list:
    print(i[::-1])
