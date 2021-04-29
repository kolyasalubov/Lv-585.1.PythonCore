def clc():
    try:
        ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph: ")
        if ch == '1':
            import Calc
        elif ch == '2':
            import Quadratic_calculator
        elif ch == '3':
            import Graf
        else:
            raise ValueError("You must enter a number in the range 1-3")
    except ValueError as e: 
        print(e)
print (clc())

