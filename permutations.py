import itertools
n=input("enter number")
s=list(itertools.permutations(n))
for i in s:
 print(''.join(i))
