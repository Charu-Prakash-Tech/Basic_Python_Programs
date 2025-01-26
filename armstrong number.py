def num(arm):
    sum=0
    dig=str(arm)
    digi=len(dig)
    for d in dig:
        sum += int(d) ** digi
    return sum==arm
Number=int(input("Enter the number : "))
if num(Number):
    print(Number,"is a armstrong number")
else:
    print(Number,"is a not an armstrong number")