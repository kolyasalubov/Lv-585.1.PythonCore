def rectangle_square():
    """
    rectangle_square - function
    Input parameter - sides of the rectangle
    Input parameter type - float
    Function calculates and returns the square of ​​a rectangle
    """

    a = float(input("Rectangle length: "))
    b = float(input("Rectangle width: "))
    return a * b

def triangle_square():
    """
    triangle_square - function
    Input parameter - the base and the heigh of the triangle
    Input parameter type - float
    Function calculates and returns the square of ​​a triangle
    """

    b = float(input("Triangle base: "))
    h = float(input("Triangle height: "))
    return 0.5 * h * b

def circle_square():
    """
    circle_square - function
    Input parameter - the radius of a circle
    Input parameter type - float
    Function calculates and returns the square of ​​a circle
    """

    PI = 3.14
    r = float(input("The radius of a circle: "))
    return PI * r ** 2

def square():
    """
    square - function
    Input parameter - type of the figure
    Input parameter type - str
    Function calculates and returns the area of the figure selected by the user.
    """

    user_choice = input("Choose  the figure. Rectangle is '1', triangle is '2' and circle is '3': ")
    if user_choice == "1":
        return rectangle_square()
    elif user_choice == "2":
        return triangle_square()
    elif user_choice == "3":
        return circle_square()
    else:
        return "Incorrect value!"

print(square())
