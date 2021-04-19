even_two_div_list = [number for number in range(1, 11) if number%2 == 0]
odd_three_div_list = [number for number in range(1, 11) if number%2 != 0 and number%3 == 0]
two_three_undiv_list = [number for number in range(1, 11) if number%2 != 0 and number%3 != 0]
print(f"\nEven numbers that are divisible by 2 are {even_two_div_list}.\
     \n\nOdd numbers, which are divisible by 3 {odd_three_div_list}.\
    \n\nNumbers that are not divisible by 2 and 3 are {two_three_undiv_list}.\n")
