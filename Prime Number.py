while True:
    user=input("Enter the number : ")
    try:
        num=int(user)
    except ValueError:
        print("Enter the valid number")
        continue
    flag=0
    if num<2:
        flag=1
    else:
        for i in range(2,num):
            if num%i==0:
                flag=1
                break
    if flag==1:
        print("The number" ,num, "is not a prime number")
    else:
        print("The number" ,num, "is a prime number")
    break