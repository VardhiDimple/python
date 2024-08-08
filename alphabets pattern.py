n=int(input("enter no"))
current=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(current),end="")
        current+=1
    print()
    
