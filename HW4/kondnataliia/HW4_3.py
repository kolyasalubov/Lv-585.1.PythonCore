user_number = int(input("Enter your number: "))
fibonacci_sequence = [0, 1]
while len(fibonacci_sequence):
    fibonacci_sequence.append(fibonacci_sequence[-2]+fibonacci_sequence[-1])
    if fibonacci_sequence[-1] >= user_number:
        break 
print(f"Your Fibonacci sequence is {fibonacci_sequence}.")
