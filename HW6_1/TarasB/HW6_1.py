def The_Largest_Number (number1, number2):
    """
    This function returns
    the largest number of two
    """
    if int(number1) == int(number2):
        print(f"Your number {number1} is equal to {number2}")
        return The_Largest_Number
    elif number1 < number2:
        print(f"Your number {number1} is smaller than {number2}")
        return The_Largest_Number
    else:
        print(f"Your numbers {number1} is bigger than {number2}")
        return The_Largest_Number

print(The_Largest_Number(101, 202))