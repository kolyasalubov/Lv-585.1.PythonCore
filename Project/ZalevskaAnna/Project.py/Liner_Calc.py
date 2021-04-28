def calc():
    a = float(input("Enter a "))
    b = float(input("Enter b "))
    if a == 0 and b == 0:
        print("An infinite number of solutions.")
    if a == 0 and b != 0:
        print("There are no solutions.")
    if a != 0:
        print(b/a)
        