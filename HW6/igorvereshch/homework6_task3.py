pi = 3.14

def area_of_rectangle():
    height = int(input("Введіть висоту прямокутника: "))
    width = int(input("Введіть ширину прямокутника: "))
    print(f"Площа прямокутника з висотою {height} та шириною {width} дорівнює {height * width}.")

def area_of_triangle():
    height = int(input("Введіть висоту трикутника: "))
    side = int(input("Введіть сторону трикутника: "))
    print(f"Площа трикутника з висотою {height}, проведеною до сторони довжиною {side}" +\
          f" дорівнює {0.5 * height * side}.")

def area_of_circle():
    radius = int(input("Введіть радіус кола: "))
    print(f"Площа кола з радіусом {radius} дорівнює {pi * radius ** 2}.")

figure = input("Введіть назву фігури, площу якої бажаєте знайти: ")
if figure == "прямокутник":
    area_of_rectangle()
elif figure == "трикутник":
    area_of_triangle()
elif figure == "коло":
    area_of_circle()
else:
    print("Неправильна назва фігури або така фігура ще не підтримується.")