even_num = [value for value in range(1,11) if value%2 == 0]
odd_num = [value for value in range(1,11) if  value%2 !=0 and value%3 == 0]
other_num = [value for value in range(1,11) if value%2 !=0 and value%3 != 0]

print(f"even numbers that are divisible by 2: {even_num}")
print(f"odd numbers, which are divisible by 3: {odd_num}")
print(f"numbers that are not divisible by 2 and 3: {other_num}")