def fact(n):
    if n==1 or n==0:
        return 1
    result=1
    for i in range(2,n+1):
        result*=i
    return result
user_input=input("Enter the number : ")
change=str(user_input)
sum=0
for i in change:
    sum+=fact(int(i))
if sum==int(user_input):
    print("strong number")
else:
    print("not a strong number")