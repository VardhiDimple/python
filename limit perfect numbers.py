a=3
n=2
t=[]
while len(t)<a:
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum+=i
    if sum==n:
        t.append(i)
    n=n+1
print(t)
    
