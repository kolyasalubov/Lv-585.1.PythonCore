import math

def rectangle_square(a, b):
    """
    Function calculates and returns the square of ​​a rectangle.
    """

    a = float(input("Rectangle length: "))
    b = float(input("Rectangle width: "))
    return a * b

def triangle_square():
    """
    Function calculates and returns the square of ​​a triangle.
    """

    b = float(input("Triangle base: "))
    h = float(input("Triangle height: "))
    return 0.5 * h * b

def circle_square():
    """
    Function calculates and returns the square of ​​a circle.
    """

    r = float(input("The radius of a circle: "))
    return math.pi * math.pow(r, 2)
