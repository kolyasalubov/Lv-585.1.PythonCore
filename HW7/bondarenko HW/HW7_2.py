import re

def is_valid(password):
    pattern = r"(?=.*[$#@])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=^.{6,16}$)"
    if re.search(pattern, password):
        return 'valid'
    return 'invalid'




#random from 1 to 100
#import random

#number = random.randint(1, 100)
#print(number)

#guess = int(input("Guess the number between 1 and 100:\n"))

#while True:
#    if guess == number:
#        print("You win!!!")
#        break
#    elif guess < number:
#        guess = int(input("Choose larger number!"))
#    else:
#       guess = int(input("Choose smaller number!"))


