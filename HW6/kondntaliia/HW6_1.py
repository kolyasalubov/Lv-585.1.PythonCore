def return_largest_number(number1, number2):
    """
    This function returns 
    the largest number of two numbers.
    """

    return int(max([number1, number2]))

print(f"The largest number is {return_largest_number(int(input('1st number: ')), int(input('Enter 2nd number: ')))}.")
