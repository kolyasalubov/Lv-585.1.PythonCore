# Write a program that calculates the square of ​​a rectangle, triangle and circle (write three functions to calculate the square, and call them in the main program depending on the user's choice).

def return_rectangle_square ():
    h = float(input("Rectangle high: "))
    w = float(input("Rectange width: "))
    return "Square of rectangle is {}".format(h*w)

def return_triangle_square():
    t = float(input("Triangle hign: "))
    r = float(input("Triangle basis: "))
    return "Square of triangle is {}".format (0.5 * t * r)
def return_circle_square():
    PI = 3.14
    c = float(input("Input basis: "))
    return "Square of a circle is {}".format (PI*c**2)

figure = input("1 - rectangle, 2 - triangle, 3 - circle: ")
if figure == '1':
    print (return_rectangle_square())
elif figure == '2':
    print (return_triangle_square())
elif figure == '3':
    print (return_circle_square())
else:
    print ("Your choice is incorrect")
