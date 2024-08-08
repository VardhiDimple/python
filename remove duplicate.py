a=[1,2,2,3,4,5,4]
b=sorted(a)
c=[]
d=[]
for i in b:
    if i in c and i not in d:
        d.append(i)
    c.append(i)
print(d)
