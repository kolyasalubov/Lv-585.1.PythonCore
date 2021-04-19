even_num = 10
print("Numbers that are divisible by 2 : ")
for x in range(1, even_num +1):
    if x % 2 == 0:
        print(x)



odd_num = 10
print("Numbers, which are divisible by 3 : ")
for y in range (1, odd_num, +2):
    if y % 3 == 0:
        print(y)



all_num = 10
print("Numbers that are not divisible by 2 and 3 : ")
for i in range(1, all_num, 2):
    if i % 2 and 3 != 0:
       print(i)

