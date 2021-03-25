number = int(input("Enter a four-digit number: "))

print(f"\nWe have the number {number}.\n")
digit1 = number % 10
digit2 = number % 100 // 10
digit3 = number % 1000 // 100
digit4 = number // 1000
mult = digit4 * digit3 * digit2 * digit1
print(f"The multiplicated number is {mult}.\n")

str_number = str(number)
reversed_number = str_number[::-1]
print(f"The number written in reverse order is {reversed_number}.\n")

sorted_number = sorted(str_number)
str_number = "".join(sorted_number)
print(f"The sorted digits of this number are as follows: {str_number}.\n")
