n=153
d=[int(digit)for digit in str(n)]
sum=0
for i in d:
    sum=sum+i**3
if(sum==n):
    print("armsstrong")
else:
    print("not")
    
