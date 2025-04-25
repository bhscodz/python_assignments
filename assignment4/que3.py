import string 
s=input()
s=s.replace(" ",'')
s=s.lower()
pangram=True
for i in string.ascii_lowercase:
    if i not in s:
        pangram=False
        break
if pangram:
    print("pangram")
else:
    print("not pangram")
