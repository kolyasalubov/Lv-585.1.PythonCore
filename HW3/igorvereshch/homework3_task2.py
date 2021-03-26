numbr = input("Enter a 4-digit number:")

# 1. Через стрічки
product = int(numbr[0]) * int(numbr[1]) * int(numbr[2]) * int(numbr[3])
inverted = int(numbr[3] + numbr[2] + numbr[1] + numbr[0])
print(f"Число {numbr}")
print("1. Використання стрічок.") 
print(f"Добуток цифр числа дорівнює {product}")
print(f"Запис числа в зворотньому порядку: {inverted}")
numbr_list = [numbr[0],numbr[1],numbr[2],numbr[3]]
numbr_list.sort()
sorted_numbr = int(numbr_list[0] + numbr_list[1] + numbr_list[2] + numbr_list[3])
print(f"Сортоване число (цифри в порядку зростання): {sorted_numbr}")

# 2. Через лист
numbr_int = int(numbr)
numbr_list = []
numbr_list.append(numbr_int % 10)
numbr_int //= 10
numbr_list.append(numbr_int % 10)
numbr_int //= 10
numbr_list.append(numbr_int % 10)
numbr_int //= 10
numbr_list.append(numbr_int % 10)
product = numbr_list[0] * numbr_list[1] * numbr_list[2] * numbr_list[3]
inverted = 1000 * numbr_list[0] + 100 * numbr_list[1] + 10 * numbr_list[2] + 1 * numbr_list[3]
print("_____________________________________________________________")
print("2. Використання list")
print("Добуток цифр числа дорівнює {0}".format(product))
print("Запис числа в зворотньому порядку: {0}".format(inverted))
numbr_list.sort(reverse = True)
sorted_numbr = 1000 * numbr_list[0] + 100 * numbr_list[1] + 10 * numbr_list[2] + 1 * numbr_list[3]
print("Сортоване число (цифри в порядку спадання): {0}".format(sorted_numbr))