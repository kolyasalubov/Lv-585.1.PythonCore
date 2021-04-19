import math


def area_of_rectangle(a,b):
     a = float(input(" Enter rectangle lenght: "))
     b = float(input(" Enter rectangle width: "))
     return a * b


def area_of_triangle():
    a = float(input(" Enter triangle base: "))
    h = float(input(" Enter triangle height: "))
    return 0.5 * h * a


def area_of_circle():
    r = float(input(" Enter circle radius: "))
    return math.pi * math.pow(r, 2)

