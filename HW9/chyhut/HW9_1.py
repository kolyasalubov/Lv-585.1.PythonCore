def age_person(age):
    age = input("Enter your age: ")
    if age < 0:
        raise ValueError("Only positive number")
    if age % 2 == 0:
        print("Your {age} is even")
    else:
        print("Your {age} is odd")
