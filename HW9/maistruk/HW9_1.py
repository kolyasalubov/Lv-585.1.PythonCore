try:
    user_age = int(input("Please, provide your age: "))
    if user_age > 0 and user_age %2 == 0:
        print("Your age is even")
    elif user_age > 0 and user_age % 2 != 0:
        print("Your age is odd")
    if user_age < 0:
        raise ValueError ("Your age have incorrect input!")
except ValueError as e:
    print(e)
