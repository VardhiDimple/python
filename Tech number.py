n=3025
s=str(n)
a=s[:len(s)//2]
b=s[len(s)//2:]
c=int(a)+int(b)
d=c**2
if(d==n):
    print("tech")
else:
    print("not")
