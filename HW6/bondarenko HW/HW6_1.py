def return_max_number(number1, number2):
    '''
    return_number - function
    input parametet - numbers
    type input parameter - int

    '''
    number1 = float(number1)
    number2 = float(number2)

    if number1 == number2:
        return f"{number1} is equal to {number2}"
    if number1 > number2:
        return f"max number is {number1}"
    else:
        return f"max number is {number2}"

print(return_max_number(10, 20))

print(return_max_number.__doc__)

print(return_max_number.__code__)