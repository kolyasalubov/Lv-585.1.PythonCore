
odd_not_divided_3 = [x for x in range(1,11) if x % 2 != 0 and x % 3 !=0] 

even = [x for x in range(1,11) if x % 2 == 0] 

divided_3 = [x for x in range(1,11) if x % 3 == 0 and x % 2 !=0]

print(f"Numbers that are not divisible by 2 and 3:\n{odd_not_divided_3}\n Even numbers divisible by 2:\n{even}\n Odd numbers divisible by 3:\n{divided_3}")
