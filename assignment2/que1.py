string=input("enter the string ")
print("".join(list(map(lambda y,x:y.upper() if(x%2!=0) else (y),string,range(len(string))))))