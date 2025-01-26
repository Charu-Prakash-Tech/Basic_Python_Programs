while True:
    user=input("Enter the number : ")
    try:
        num=int(user)
    except ValueError:
        print("Enter the valid input")
        continue
    sum=0
    con=str(num)
    for i in con:
        sum=sum+int(i)
    print(sum)
    break


