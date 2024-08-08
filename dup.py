n=[1,2,3,7,7,8,8]
target=7
start=-1
end=-1
for i in range(len(n)):
 if (n[i]==target):
  if start==-1:
   start=i
  end=i
result=[start,end]
print(result)
    
