def clc():
    ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph, 0 - Exit: ")
    while True:
        try:
            if ch == '1':
                import Calc
                ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph, 0 - Exit: ")
            elif ch == '2':
                import Quadratic_calculator
                ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph, 0 - Exit: ")
            elif ch == '3':
                import Graf
                ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph, 0 - Exit: ")
            elif ch == '0':
                break
            else:
                raise ValueError("You must enter a number in the range 1-3")
        except ValueError as e: 
            print(e)
            ch = input("1 - Ordinary calculator, 2 - Quadratic calculator, 3 - Draw a graph, 0 - Exit: ")
print (clc())

