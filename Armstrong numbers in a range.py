def num(arm):
    sum=0
    dig=str(arm)
    digi=len(dig)
    for d in dig:
        sum += int(d) ** digi
    return sum==arm
Number=int(input("Enter the first number : "))
Number1=int(input("Enter the second number :"))
arms=[]
for x in range(Number,Number1):
    if num(x):
        arms.append(x)
print(arms)
