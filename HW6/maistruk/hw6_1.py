#Task1. Write a function that returns the largest number of two numbers (use DocStrings documentation strings in the function).

def my_num (entire_number1, entire_number2):
    """This function will return 
       the largest number of two 
       entered by user
       """
    if entire_number1 > entire_number2:
        print (f"Your number {entire_number1} is bigger than {entire_number2}")
        return my_num
    elif entire_number1 < entire_number2:
        print (f"Your number {entire_number1} is smaler than {entire_number2}")
        return my_num
    else:
        print(f"Your numbers {entire_number1} and {entire_number2} are equal")
        return my_num

print (my_num(54, 65))

print (my_num.__doc__)










#Write a function that returns the arithmetic mean of any number of numbers.

# def obtain_arithmetic_mean (*args):
#     """the function will calculate obtain arithmetic mean mean of numbers"""
#      return f"Result: {sum(args)/ len / len(args)}"

