def digital_root(num):
    if (num//10==0):
        return num
    count =0
    for i in str(num):
        count+=int(i)
    return digital_root(count)

print(digital_root(int(input("enter the number"))))