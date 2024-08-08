n=[1,2,3,4,5,1,2,3,4]
x=[]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j] and n[i] not in x:
            x.append(n[i])
print(x)
