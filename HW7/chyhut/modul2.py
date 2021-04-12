import squarefigures

def square_of_figure():
    figure = input("1-rectangle, 2-triangle, 3-circle: ")
    if figure == '1':
        return squarefigures.square_of_rectangle()
    if figure == '2':
        return squarefigures.square_of_triangle()
    if figure == '3':
        return squarefigures.square_of_circle()
    else:
        return "Input error"

w = square_of_figure()
print(w)