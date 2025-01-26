while True:
    value1=input("Enter the First Number : ")
    value2=input("Enter the Second Number : ")
    try:
        num1=int(value1)
        num2=int(value2)
    except ValueError:
        print("Enter the valid number")
        continue
    Greatest=(max(num1,num2))
    print("The greatest number is ",Greatest)
    break
