n=3025
seen=set()
while n!=1 and n not in seen:
    seen.add(n)
    n=sum(int(digit)**2 for digit in str(n))
if(n==1):
    print("happy")
else:
    print("not")
