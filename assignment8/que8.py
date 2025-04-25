s=input("enter the string")
import string
def convert(s):
    return ''.join(list(map(lambda x:str(ord(x)-96),s)))
s=convert(s)
patterns=[]
while(1):
    num=s.find('0')
    if(num==-1):
        break
    

