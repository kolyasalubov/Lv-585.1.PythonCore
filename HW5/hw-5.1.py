


n = int(input("Введіть число: "))

odd = 0
even = 0
not_dsbl = 0

for i in range(n+1):
    if i%2 == 0 and i // 2:
        even += 1
    elif i% 2 != 0 and i%3 == 0:
        odd += 1
    elif i%2 != 0 and i%3 != 0:
        not_dsbl += 1
print("Even: %d, odd: %d, not_dsbl: %d" % (even, odd, not_dsbl))
