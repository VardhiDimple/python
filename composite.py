n=8
d=0
for i in range(1,n+1):
    if(n%i==0):
        d=d+1
if(d>2):
    print("composite")
else:
    print("not")
