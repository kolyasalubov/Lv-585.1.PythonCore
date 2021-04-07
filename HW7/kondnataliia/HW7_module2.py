import module1
user_choice = input("Choose  the figure. Rectangle is '1', triangle is '2' and circle is '3': ")


def square():
    """
    Function calculates and returns the area 
    of the figure selected by the user.
    """

    if user_choice == "1":
        return module1.rectangle_square()
    elif user_choice == "2":
        return module1.triangle_square()
    elif user_choice == "3":
        return module1.circle_square()
    else:
        return "Incorrect value!"

print(square())
