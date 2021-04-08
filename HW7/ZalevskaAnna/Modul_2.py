import Modul_1
def figure():
    figure = input("1-rectangle, 2-triangle, 3-circle: ")
    if figure == '1':
        return Modul_1.return_square_rectangle()
    if figure == '2':
        return Modul_1.return_square_triangle()
    if figure == '3':
        return Modul_1.return_square_circle()
    else:
        return "Input error"
print(figure())
