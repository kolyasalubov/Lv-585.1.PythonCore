age = int(input("Enter your age: "))

def userAge(age):
    try:
        if age > 0:
            if age % 2 == 0:
                return(f"Your age ({age}) is an even number.")
            else:
                return(f"Your age ({age}) is an odd number.")
        if age < 0:
            raise ValueError ("Age cannot be negative!")
    except ValueError as e:
        return(e)
print(userAge(age))
