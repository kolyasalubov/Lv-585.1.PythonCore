import area

print("Вітаємо у програмі для пошуку площ фігур. Наразі доступні прямокутник, трикутник та коло.\n" + \
      "Назви можна вводити англійською, а саме: rectangle, triangle, circle відповідно.")
figure = input("Введіть бажану фігуру: ")
if figure == "прямокутник" or figure == "rectangle":
    area.area_of_rectangle()
elif figure == "трикутник" or figure == "triangle":
    area.area_of_triangle()
elif figure == "коло" or figure == "circle":
    area.area_of_circle()
else:
    print("Неправильно введені дані.")