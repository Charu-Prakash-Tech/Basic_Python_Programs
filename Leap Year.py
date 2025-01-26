while True:
    user=input("Enter the year : ")
    try:
        year=int(user)
    except ValueError:
        print("Enter the valid year")
        continue
    if year%4==0 or year%400==0 and year%100!=0:
        print("The year" ,year, "is a leap year")
    else:
        print("The year" ,year, "is not a leap year")
    break
        