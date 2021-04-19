# Не знаю чи ця конструкція переганяє наш матеріал
# Але в розв'язках в Codewars вона зустрічається постійно
list1 = [i ** 2 - 3 * i - 6 for i in range(10)]
for i in range(len(list1)):
    list1[i] = list1[i] + 0.0
print(list1)