import random

number = random.randint(1, 100)
print (a)

user_number = float(input("Enter your number: ")

while True:
    if user_number > number:
        return (float(input("You are close!Try lower number: ")))
    elif user_number < number :
        return (float(input("You are close!Try higher number: ")))
    elif user_number == number:
        return ("Good job!")
    else:
        print ("Error")