name = ""
while name != "First":
    name = input("Введіть будь-ласка ім'я користувача: ")
    if name != "First":
        print("Вибачте, інформація введена неправильно. Спробуйте ще раз.")
print(f"Вітаємо, {name}!")