def factorial(n):
 for i in range(1,n+1):
  if n==0 or n==1:
   return 1
  if(n>1):
   return n*factorial(n-1)
n=int(input("n"))
sum=0
for i  in range(1,n+1):
 sum=sum+factorial(i)
print(sum)
