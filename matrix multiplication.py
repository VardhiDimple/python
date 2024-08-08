a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        for r in range(len(result)):
            result[i][j]=a[i][j]*b[i][j]
for k in result:
    print(k)
            
