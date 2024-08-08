m=[[1,2,3],[4,5,6],[7,8,9]]
r_sum=0
c_sum=0
d_sum=0
for i in range(len(m)):
 for j in range(len(m)):
  r_sum=r_sum+m[i][j]
  print("sum of",i,"th row",r_sum)
  r_sum=0
for i in range(len(m)):
 for j in range(len(m)):
  c_sum=+m[j][i]
  print("sum of",i,"th column",c_sum)
  c_sum=0
for i in range(len(m)):
 for j in range(len(m)):
  if(i==j):
    d_sum=+m[i][j]
  print ("sum of",i,"th diagonal is",d_sum)
  
