m=[[1,2],[5,3]]
n=[[2,3],[4,1]]
result=[[0,0],[0,0]]
for i in range(len(m)):
    for j in range(len(n)):
        for k in range(len(result)):
            result[i][j]=m[i][k]*n[k][i]
for r in result:
    print(r)
