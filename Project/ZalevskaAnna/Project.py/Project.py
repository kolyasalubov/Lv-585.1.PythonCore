import Liner_Calc
def clc():
    ch = input("1 - Ordinary calculator, 2 - linear calculator, 3 - Quadratic calculator, 4 - Draw a graph: ")
    if ch == '1':
        import Calc
    elif ch == '2':
        return Liner_Calc.calc()
    elif ch == '3':
        import Quadratic_calculator
    elif ch == '4':
        import Graf
    else:
        return "Input error"
print (clc())

