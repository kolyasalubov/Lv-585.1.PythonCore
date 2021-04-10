#Task2. In the range from 1 to 10 determine even numbers that are divisible by 2,odd numbers, which are divisible by 3, numbers that are not divisible by 2 and 3.

var_1 = [n for n in range(1, 11) if n%2 == 0]
print (var_1)
var_2 = [n for n in range (1, 11) if n%2 != 0 and n%3 == 0]
print (var_2)
var_3 = [n for n in range (1, 11) if n%2 != 0 and n%3 != 0]
print (f"Even numbers is: {var_1},\n Odd numbers is: {var_2},\n Numbers that are not divisible by 2 and 3 is: {var_3}")