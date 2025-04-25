product_list={}
print("enter the name of product and prices enter -1 to exit")
while 1:
    name=input("enter product name:")
    if(name=="-1"):
        break
    product_list[name]=int(input("enter the price of product:"));

print("view product by entring name enter -1 to exit")
while True:
    name=input("enter product name")
    if(name=="-1"):
        break
    if name in product_list:
        print(f"item {name}, price:{product_list[name]}")
    else:
        print("product not found")