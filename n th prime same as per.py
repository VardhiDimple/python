n=4
p=[]
m=2
while(len(p)<n):
    is_prime=True
    for i in range(2,m):
        if(m%i==0):
            is_prime=False
            break
    if is_prime:
        p.append(m)
    m=m+1
print(p)
