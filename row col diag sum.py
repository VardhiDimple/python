m=[[1,2],[3,4]]
r_sum=0
c_sum=0
d_sum=0
for i in range(len(m)):
    for j in range (len(m)):
        r_sum+=m[i][j]
    print(r_sum)
    r_sum=0
        for i in range(len(m)):
            for j in range(len(m)):
                c_sum+=m[i][j]
            print(c_sum)
                c_sum=0
                for i in range(len(m)):
                    for j in range(len(m)):
                        if(i==j):
                            d_sum+=m[i][j]
                        print(d_sum)
