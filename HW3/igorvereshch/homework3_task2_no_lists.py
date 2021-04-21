# Вирішив спробувати розв'язати це завдання (лекція 3, завдання 2) без списку
# бо маю багато вільного часу і не знав про Codewars.
# Ще є такий момент що цей випадок спрацює і з числами меншими від 1000
# але тоді всі відсутні цифри будуть присвоєні 0
# Якщо знайдете число яке не спрацює, пишіть.

numbr_int = 5157
digit0 = numbr_int % 10
digit1 = (numbr_int // 10) % 10
digit2 = (numbr_int // 100) % 10
digit3 = numbr_int // 1000
product = digit0 * digit1 * digit2 * digit3
inverted = 1000 * digit0 + 100 * digit1 + 10 * digit2 + 1 * digit3

# Думаю що тут потрібне пояснення що взагалі відбуватиметься далі.
# Кожна з величин D_0, D_1, D_2, D_3 визначає кількість повторень
# відповідної цифри (digit0, digit1, digit2, digit3) в нашому числі
# і дорівнює нулю якщо ця цифра врахована в одному з попередніх D.
# Після чого кожне з чисел D використовується для створення коефіцієнтів
# coeficient_0..3 (відповідно), кожен з яких дорівнює 1111...11 де
# кількість одиниць дорівнює відповідному коефіцієнту D (в разі якщо
# D = 0 величина coeficient також рівна 0). Ці коефіцієнти використовуються
# для створення сортованого числа.
# Приклад (число в прикладі дорівнює 5157, надалі всі коментарі по прикладу):
# digit0 = 7
# digit1 = 5
# digit2 = 1
# digit3 = 5 

D_0 = 1 + (digit0 == digit1) + (digit0 == digit2) + (digit0 == digit3)
D_1 = (digit0 != digit1) * (1 + (digit1 == digit2) + (digit1 == digit3))
D_2 = (digit0 != digit2) * (digit1 != digit2) * (1 + (digit2 == digit3))
D_3 = (digit0 != digit3) * (digit1 != digit3) * (digit2 != digit3)

# Відповідно по цим формулам:
# D_0 = 1 + (7 == 5) + (7 == 1) + (7 == 5) = 1 + 0 + 0 + 0 = 1
# D_1 = (7 != 5) * (1 + (5 == 1) + (5 == 5)) = 1 * (1 + 0 + 1) = 2
# D_2 = (7 != 1) * (7 != 5) * (1 + (1 == 5)) = 1 * 1 * (1 + 0) = 1
# D_3 = (7 != 5) * (5 != 5) * (1 != 5) = 1 * 0 * 1 = 0

coeficient_0 = int(str(bin(2 ** D_0 - 1)).replace("0b",""))
coeficient_1 = int(str(bin(2 ** D_1 - 1)).replace("0b",""))
coeficient_2 = int(str(bin(2 ** D_2 - 1)).replace("0b",""))
coeficient_3 = int(str(bin(2 ** D_3 - 1)).replace("0b",""))

# Бінарні числа переводяться у стрічку вигляду "0b<набір 1 та 0>". 
# Команда replace("0b","") використовується для видалення частини "0b"
# інакше команда int не спрацює.
# Відповідні коефіцієнти:
# coeficient_0 = int(str(bin(2^1 - 1)).replace("0b","")) = int(str(bin(1)).replace("0b","")) =
#              = int("0b1".replace("0b","")) = int("1") = 1
# coeficient_1 = int(str(bin(2^2 - 1)).replace("0b","")) = int(str(bin(3)).replace("0b","")) =
#              = int("0b11".replace("0b","")) = int("11") = 11
# coeficient_2 = 1 (обчислення ті самі що й в coeficient_0)
# coeficient_3 = 0 (кому цікаво, можете переконатись в цьому самі)

# Тепер власне до створення сортованого числа. 
# Добуток digit0(1, 2, 3) * coeficient0(1, 2, 3) 'групує' однакові цифри в одному додатку 
# і відкидає решту додатків що використовують це число.
# В нашому випадку digit1 = digit3 = 5 і обидві цифри будуть 'згруповані' в 1-му додатку:
# digit1 * coeficient_1 = 5 * 11 = 55
# і відкинуть 3-й додаток:
# digit3 * coeficient_3 = 5 * 0 = 0
# Якщо цифра зустрчається в числі 1 раз, то coeficient ні на що не впливає (бо він буде рівний 1):
# digit0 * coeficient_0 = 7 * 1 = 7
# digit2 * coeficient_2 = 1 * 1 = 1

# Будь-яке 4-значне число можна записати в наступному вигляді: 
# 1000 * <цифра3> + 100 * <цифра2> + 10 * <цифра1> + 1 * <цифра0>
# Довгі вирази з нерівностями відповідають за те на якому місці яка цифра буде стояти.
# У нашому прикладі кожен з цих виразів буде дорівнювати:
# для digit0: ((7 < 5) + (7 < 1) + (7 < 5)) = 0
#     digit1: ((5 < 7) + (5 < 1) + (5 < 5)) = 1
#     digit2: ((1 < 7) + (1 < 5) + (1 < 5)) = 3
#     digit3: ((5 < 7) + (5 < 1) + (5 < 5)) = 1
# Використовуючи те, що 10 ** 0 = 1; 10 ** 1 = 10; 10 ** 2 = 100; 10 ** 3 = 1000
# отримуємо наступний результат:
# sorted_number = 7 * 10 ** 0 + 55 * 10 ** 1 + 1 * 10 ** 3 + 0 * 10 ** 1 =
#               = 7 + 550 + 1000 = 1557

sorted_numbr = digit0 * coeficient_0 * 10 ** ((digit0 < digit1) + (digit0 < digit2) + (digit0 < digit3)) +\
               digit1 * coeficient_1 * 10 ** ((digit1 < digit0) + (digit1 < digit2) + (digit1 < digit3)) +\
               digit2 * coeficient_2 * 10 ** ((digit2 < digit0) + (digit2 < digit1) + (digit2 < digit3)) +\
               digit3 * coeficient_3 * 10 ** ((digit3 < digit0) + (digit3 < digit1) + (digit3 < digit2))

# Для сортування цифр в порядку спадання достатньо всі знаки '<' поміняти на '>'

print("_____________________________________________________________")
print("3. Без string або list")
print("Добуток цифр числа дорівнює", product)
print("Запис числа в зворотньому порядку:", inverted)
print("Сортоване число (цифри в порядку зростання):", sorted_numbr)