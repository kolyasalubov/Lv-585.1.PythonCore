import math

def square_of_rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "square of rectangle is = {}".format(a*b)

def square_of_triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "square of triangle is = {}".format(0.5 * a *h)

def square_of_circle():
    r = float(input("Input radius: "))
    return "square of circle is = {}".format(math.pi * math.pow(r, 2))