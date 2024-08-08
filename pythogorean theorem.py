l=20
t=[]
for a in range(1,l):
    for b in range(a,l):
        for c in range(b,l):
            if a**2+b**2==c**2:
                t.append((a,b,c))
                print(t,end="")
