n=int(input("enter number"))
s=""
while(n>0):
    r=n%2
    s=str(r)+s
    n=n//2
print(s)
