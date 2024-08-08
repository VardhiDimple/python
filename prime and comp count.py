n=[4,54,29,71,7,59,98,23]
p=0
c=0
for i in n:
    if(i>1):
        d=0
    for j in range(2,i):
        if(i%j==0):
            d=d+i
    if(d>2):
        p+=1
    else:
        c+=1
print(p,c)
                    
