n = int(input("Введіть ваше число: "))
n = int(n)

f1 = 1
f2 = 1
i = 0
while i < n - 2:
    f = f1 + f2
    f1 = f2
    f2 = f
    i += 1
print(f2)