


n = int(input("Введіть число: "))

odd = []
even = []
not_dsbl = []

for i in range(n+1):
    if i%2 == 0:
        even.append(i)
    elif i%3 == 0:
        odd.append(i)
    else:
        not_dsbl.append(i)
print("even: ", even)
print("odd: ", odd)
print("not_desbl: ", not_dsbl)
