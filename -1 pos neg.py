p_sum=0
n_sum=0
p_count=0
n_count=0
while True:
    n=int(input("enter number"))
    if n==-1:
        break
    if n>0:
        p_sum+=n
        p_count+=1
    elif(n<0):
        n_sum+=n
        n_count+=1
if p_sum>0:
    p_avg=p_sum/p_count
else:
    print("no sum")
if n_sum>0:
    n_avg=n_sum/n_count
else:
    print("no neg")
