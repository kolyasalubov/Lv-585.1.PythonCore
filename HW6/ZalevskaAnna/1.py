def Largest_Number(num1, num2):
    """This function returns a larger number"""
    if int(num1) == int(num2):
        return "These numbers are equal"
    elif int(num1) > int(num2):
        return num1
    else:
        return num2
print(Largest_Number(5, 6))