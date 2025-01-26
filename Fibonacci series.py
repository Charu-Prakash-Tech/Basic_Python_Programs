f1=0
f2=1
f=[f1,f2]
num=5
for i in range(1,num):
    f3=f1+f2
    f.append(f3)
    f1=f2
    f2=f3
print(f)