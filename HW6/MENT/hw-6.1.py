def mylargest_number(number1, number2):
    """
     I write a function, that returns the largest number of two numbers

    """

    return int(max([number1, number2]))

print(f"Largest number: {mylargest_number(int(input('Enter number1: ')), int(input('Enter number2: ')))}.")