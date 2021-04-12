delitsa_na_dva = []
delitsa_na_2 = []
delitsa_na_3 = []
nedelitsa = []

for a in range (1, 10):    

    if a % 3 == 0:
        delitsa_na_3.append(a)
    elif a % 2 == 0:
            delitsa_na_2.append(a)
    else:
            nedelitsa.append(a)

print(delitsa_na_2)
print(delitsa_na_3)
print(nedelitsa)

