n = [64, 34, 25, 12, 22, 11, 90]
a = len(n)
for i in range(a):
    for j in range(0, a-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]

print(n)

