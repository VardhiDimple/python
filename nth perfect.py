n=4
p=[]
m=2
while len(p)<n:
    sum=0
    for i in range(1,m):
        if(m%i==0):
            sum=sum+i
    if sum==m:
        p.append(m)
    m=m+1
print(p)
