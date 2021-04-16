try:
    age = int(input("Age: "))
    if age < 0:
        raise ValueError("Age can't be a negative number")
except ValueError as e:
    print(e)
except Exception as e:
    print("Something unexpected happened: ", e)
else:
    if age % 2 == 0:
        msg = "even"
    else:
        msg = "odd"
    print(f"Your age, which is {age}, is {msg} number")