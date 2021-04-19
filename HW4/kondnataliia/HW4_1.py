number = int(input("Enter your number: "))
factorial = 1
if number > 0:
    for element in range(1, number+1):
        factorial = factorial * element
    print(f"The factorial of {number} is {factorial}.")

# or

number = int(input("Enter your number: "))
factorial = 1
while number > 1:
    factorial = factorial * number
    number -= 1
print(f"The factorial of the number you entered is {factorial}.")
