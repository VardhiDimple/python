a="@gmail.com"
s=[]
for i in a:
    if not i.isalnum()and not i.isspace():
        s.append(i)
for i in s:
    print(i)
        
