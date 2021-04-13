def square_of_rectangle():
    a = float(input("Input width: "))
    b = float(input("Input height: "))
    return "square of rectangle is = {}".format(a*b)


def square_of_triangle():
    a = float(input("Input basis: "))
    h = float(input("Input height: "))
    return "square of triangle is = {}".format(0.5 * a *h)


def square_of_circle():
    PI = 3.14
    r = float(input("Input radius: "))
    return "square of circle is = {}".format(PI * r**2)


def square_of_figure():
    figure = input("1-rectangle, 2-triangle, 3-circle: ")
    if figure == '1':
        return square_of_rectangle()
    if figure == '2':
        return square_of_triangle()
    if figure == '3':
        return square_of_circle()
    else:
        return "Input error"


w = square_of_figure()
print(w)