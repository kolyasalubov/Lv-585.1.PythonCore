from random import randint
true_number = randint(0, 100)
print(true_number)
user_number = int(input("Enter a number in the range 0-100: "))
while user_number <= 100:
    if user_number == true_number:
        print("Number is correct!")
        break
    elif user_number > true_number:
        print("The number of users is greater than the correct number")
        user_number = int(input("Enter a number in the range 0-100: "))
    elif user_number < true_number:
        print("The number of users is less than the correct number")
        user_number = int(input("Enter a number in the range 0-100: "))
else:
    print("Error!")   