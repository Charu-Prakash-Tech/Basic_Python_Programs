while True:
    value1=input("Enter the first number : ")
    value2=input("Enter the second number : ")
    try:
        num1=int(value1)
        num2=int(value2)
    except ValueError:
        print("Enter the valid number in both the fields")
        continue
    sum=0
    for i in range(num1,num2+1):
        sum+=i
    print(sum)
    break