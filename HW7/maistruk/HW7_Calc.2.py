import HW7_Calc

number = input ('1 - add, 2 - subtraction, 3 - multiplication, 4 - div')

if number == '1':
    print (HW7_Calc.add_numbers())
elif number == '2':
    print (HW7_Calc.sub_numbers())
elif number == '3':
    print (HW7_Calc.mul_numbers())
elif number == '4':
    print (HW7_Calc.div_numbers())
else:
    print("Incorrect number")