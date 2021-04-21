limit = 10
even = []
odd_and_divided_by_3 = []
not_divided_by_2_or_3 = []
for i in range(1, limit + 1):
    if i % 2 == 0:
        even.append(i)
    elif i % 3 == 0:
        odd_and_divided_by_3.append(i)
    else:
        not_divided_by_2_or_3.append(i)
print(f"Список чисел від 1 до {limit}, що діляться на 2: {even}")
print(f"Список непарних чисел від 1 до {limit}, що діляться на 3: {odd_and_divided_by_3}")
print(f"Список чисел від 1 до {limit}, що не діляться ні на 2, ні на 3: {not_divided_by_2_or_3}")