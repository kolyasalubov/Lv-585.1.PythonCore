


def area_of_rectangle():
    a = float(input("Enter width: "))
    b = float(input("Enter height: "))
    return "square of rectangle is = {}".format(a*b)


def area_of_triangle():
    a = float(input("Enter base: "))
    h = float(input("Enter height: "))
    return "area of triangle is = {}".format(0.5 * a *h)


def area_of_circle():
    PI = 3.14
    r = float(input("Enter radius: "))
    return "area of circle is = {}".format(PI * r**2)


def area_of_figure():
    Choice_of_figure = '1' or '2' or '3'
    Entered_Choice_of_figure = input("Choose  the figure. Rectangle is '1', triangle is '2' and circle is '3': ")
    while Entered_Choice_of_figure != Choice_of_figure:
        print("Input Error")
        Choice_of_figure = input("Choose  the figure. Rectangle is '1', triangle is '2' and circle is '3': ")
        continue
    if Choice_of_figure == '1':
        return area_of_rectangle()
    if Choice_of_figure == '2':
        return area_of_triangle()
    if Choice_of_figure == '3':
        return area_of_circle()

Y = area_of_figure()
print(Y)

