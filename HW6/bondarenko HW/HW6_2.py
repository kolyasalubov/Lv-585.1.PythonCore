def rectangle_square():
    """
    rectangle_square - function
    Input parameter - sides of the rectangle
    Input parameter type - float
    
    """

    a = float(input("Rectangle width: "))
    b = float(input("Rectangle height: "))
    return a * b

def triangle_square():
    """
    triangle_square - function
    Input parameter - the basis and the heigh of the triangle
    Input parameter type - float
    
    """

    b = float(input("Triangle basis: "))
    h = float(input("Triangle height: "))
    return 0.5 * h * b

def circle_square():
    """
    circle_square - function
    Input parameter - the radius of a circle
    Input parameter type - float
    
    """

    PI = 3.14
    r = float(input("The radius of a circle: "))
    return PI * r ** 2

def square():
    """
    square - function
    Input parameter - type of the figure
    Input parameter type - str
    
    """

    user_choice = input("Choose  the figure: Rectangle - '1', Triangle - '2' and Circle - '3': ")
    if user_choice == "1":
        return rectangle_square()
    elif user_choice == "2":
        return triangle_square()
    elif user_choice == "3":
        return circle_square()
    else:
        return "Incorrect value!"

print(square())
