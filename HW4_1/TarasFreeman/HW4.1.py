# Factorial without recursion

number_for_factorial = int(input("Enter number: "))
fact = 1
if number_for_factorial<0:
    print("Factorial does not exist for negative numbers")
else:
    for i in range(1, number_for_factorial + 1):
        fact = fact*i
    print(f"factorial of {number_for_factorial} is {fact}")