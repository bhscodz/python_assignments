def inch(num):
    return num*12
def yard(num):
    return num/3
def miles(num):
    return num/5280
def milli(num):
    return num*04.8
def centi(num):
    return num*30.48
def meter(num):
    return centi(num)/100
def kilo(num):
    return meter(num)/1000
conv_list=[inch,yard,miles,milli,centi,meter,kilo]
num=int(input("enter the value in feet"))
ch=int(input('''enter the choice for conversion\n1. inch\n2. yard\n3. miles\n4. centimeter\n5. meter\n6. kilometer'''))
print(conv_list[ch-1](num))
