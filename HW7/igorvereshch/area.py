from math import pi

def area_of_rectangle():
    height = float(input("Введіть висоту прямокутника: "))
    while height <= 0:
        print("Висота прямокутника повинна бути додатньою. Спробуйте ще раз.")
        height = float(input("Введіть висоту прямокутника: "))
    width = float(input("Введіть ширину прямокутника: "))
    while width <= 0:
        print("Ширина прямокутника повинна бути додатньою. Спробуйте ще раз.")
        width = float(input("Введіть ширину прямокутника: "))
    print(f"Площа прямокутника з висотою {height} та шириною {width} дорівнює {height * width}.")
    return height * width

def area_of_triangle():
    height = float(input("Введіть висоту трикутника: "))
    while height <= 0:
        print("Висота трикутника повинна бути додатньою. Спробуйте ще раз.")
        height = float(input("Введіть висоту трикутника: "))
    side = float(input("Введіть сторону трикутника: "))
    while side <= 0:
        print("Сторона трикутника повинна бути додатньою. Спробуйте ще раз.")
        side = float(input("Введіть сторону трикутника: "))
    print(f"Площа трикутника з висотою {height}, проведеною до сторони довжиною {side}" +\
          f" дорівнює {0.5 * height * side}.")
    return 0.5 * height * side

def area_of_circle():
    radius = float(input("Введіть радіус кола: "))
    while radius <= 0:
        print("Радіус кола повинен бути додатнім. Спробуйте ще раз.")
        radius = float(input("Введіть радіус кола: "))
    print(f"Площа кола з радіусом {radius} дорівнює {pi * radius ** 2}.")
    return pi * radius ** 2
