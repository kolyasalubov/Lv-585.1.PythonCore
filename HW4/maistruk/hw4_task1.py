#Write a script, which of the two entered numbers will determine which of them is more and which is less. Take into account the case of equality of numbers.

var_1 = float(input('Enter first number: '))
var_2 = float (input('Enter second number: '))

if var_1 == var_2:
    print (f'Entered number {var_1} is equal to second enetered number {var_2}')
elif var_1 > var_2:
    print (f'Entered number {var_1} is more than second enered number {var_2}')
else:
    print (f'Enetered number {var_1} is less than second enetered number {var_2}')