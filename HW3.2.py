#
number = input("Enter four digits number: ")
digit1 = int(number[0])
digit2 = int(number[1])
digit3 = int(number[2])
digit4 = int(number[3])
mult = digit1*digit2*digit3*digit4
print(mult)

number_list = [digit1, digit2, digit3, digit4]
numbers_sorted = sorted(number_list)
print(numbers_sorted)


x = 5
y = 10 
x, y = y, x
print("x=", x)
print("y=", y)