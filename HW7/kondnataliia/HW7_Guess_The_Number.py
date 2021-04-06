import random

intended_number = random.randint(1, 100)
user_number = int(input("Enter your number:"))

while user_number != intended_number:
    if user_number > intended_number:
        print("The intended number is less than yours.")
    else:
        print("The intended number is greater than yours.")
    user_number = int(input("Try again: "))
    
print(f"You guessed! The intended number is {user_number}!")
