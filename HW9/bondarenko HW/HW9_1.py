try:
    user_age = int(input("Enter your age: "))
    if user_age % 2 == 0:
        msg = "even"
    else:
        msg = "odd"
    print(f"{user_age} is {msg} number")
    
    if user_age <= 0:
        raise ValueError("Are you kiddging me???")
except ValueError as e:
    print(e)

