n="Saveetha School of Engineering"
a="aeiouAEIOU"
v_count=0
c_count=0
for i in n:
    if(i in a):
       v_count+=1
    else:
        c_count+=1
print(v_count,c_count)
if(v_count>c_count):
    print("v_count")
else:
    print("c_count")
