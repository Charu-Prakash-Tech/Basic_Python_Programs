while True:
    user=input("Enter the number : ")
    try:
        num=int(user)
    except ValueError:
        print("Enter the valid number : ")
        continue
    con=str(user)
    reverse=((con)[::-1])
    if user==reverse:
        print("It is a palindrome")
    else:
        print("Not a palindrome")
    break
