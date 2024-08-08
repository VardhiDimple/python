n=8
a=0
for i in range(2,n+1):
    if(n%i!=0):
        a=1
    else:
        a=0
if(a==1):
    print("prime")
else:
    print("not")
