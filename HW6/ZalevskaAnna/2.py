def return_square_rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "Square of rectangle is = {}".format(a*b)
def return_square_triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "Square of triangle is = {}".format(0.5 * a *h)
def return_square_circle():
    PI=3.14
    r = float(input("Input radius: "))
    return "Square of circle is = {}".format(PI * r**2)
def figure():
    figure = input("1-rectangle, 2-triangle, 3-circle: ")
    if figure == '1':
        return return_square_rectangle()
    if figure == '2':
        return return_square_triangle()
    if figure == '3':
        return return_square_circle()
    else:
        return "Input error"
print(figure())