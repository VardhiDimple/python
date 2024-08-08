n=int(input("enter number"))
while(n>1):
    q=n//10
    r=n%10
    sum=(q**2)+(r**2)
if (sum==1):
    print("happy")
else:
    print("not")
    
