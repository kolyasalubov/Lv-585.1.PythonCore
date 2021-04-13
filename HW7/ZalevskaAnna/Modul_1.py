import math
from math import pi
from math import pow
def return_square_rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "Square of rectangle is = {}".format(a*b)
def return_square_triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "Square of triangle is = {}".format(0.5 * a *h)
def return_square_circle():
    r = float(input("Input radius: "))
    return "Square of circle is = {}".format(pi * pow(r,2))
