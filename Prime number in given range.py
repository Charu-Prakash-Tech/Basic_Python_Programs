while True:
    user1=input("Enter the first value : ")
    user2=input("Enter the second value : ")
    try:
        low=int(user1)
        high=int(user2)
    except ValueError:
        print("Enter the valid number in both the fields")
        continue
    if low >high:
        print("First number should be higher than second number")
    p=[]
    for i in range(low,high+1):
        flag=0
        if i<2:
            continue
        if i==2:
            p.append(2)
            continue
        for x in range(2,i):
            if i%x==0:
                flag=1
                break
        if flag==0:
            p.append(i)
    print(p)
    break

