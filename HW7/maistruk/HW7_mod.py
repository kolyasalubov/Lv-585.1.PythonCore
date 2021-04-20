import math

def return_rectangle_square ():
    h = float(input("Rectangle high: "))
    w = float(input("Rectange width: "))
    return h*w

def return_triangle_square():
    t = float(input("Triangle hign: "))
    r = float(input("Triangle basis: "))
    return 0.5 * t * r
    
def return_circle_square():
    c = float(input("Input radius of circle: "))
    return math.pi*math.pow(c,2)