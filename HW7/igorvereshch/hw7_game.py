from random import randint

def game():
    '''
    Game of guessing random number from 1 to 100
    '''

    result = randint(1, 100)
    attempt = 1
    print("Вітаємо Вас у нашій грі. Ми загадали число від 1 до 100 і Ваша задача - його відгадати.")
    guess = int(input("Введіть Ваше число: "))

    while guess != result:
        if guess > 100:
            print(f"Число {guess} знаходиться за межами інтервалу від 1 до 100. Спробуйте ще раз")
        else:
            print(f"Число {guess} " + ("більше" if guess > result else "менше") +\
                   " від задуманого. Спробуйте ще раз.")
        attempt += 1
        guess = int(input("Введіть Ваше число: "))

    if attempt == 1:
        print("Неймовірно! Ви відгадали задумане число з першої спроби!")
    elif attempt < 8: 
        # Згідно з математикою, число в межі [1, 100] можна гарантовано вгадати за 7 спроб
        print(f"Чудово! Ви виграли за {attempt} спроб" + ("и" if attempt < 5 else ""))
    else:
        print("Ви молодець! Проте можна гарантовано відгадати число за 7 спроб")

game()