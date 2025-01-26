while True:
    user_input=input("Enter the Number : ")
    try:
        Number=int(user_input)
    except ValueError:
        print("Enter the Valid Number")
        continue
    sum=0
    for i in range (Number+1):
        sum+=i
    print(sum)
    break

    