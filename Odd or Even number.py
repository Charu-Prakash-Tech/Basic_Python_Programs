while True:
    user_input=input("Enter the Number : ")
    try:
        number=int(user_input)
    except ValueError:
        print("Enter the valid number")
        continue
    if number%2==0:
        print("Even Number")
    else:
        print("Odd number")
    break
