import calculator

user_choice = input("What operation do you want to perform: 1 - addition, 2 - subtraction, 3 - multiplication or 4 - division? ")
a = float(input("Enter the value a: "))
b = float(input("Enter the value b: "))

if user_choice == "1":
    print(calculator.addition(a, b))
elif user_choice == "2":
    print(calculator.subtraction(a, b))
elif user_choice == "3":
    print(calculator.multiplication(a, b))
elif user_choice == "4":
    print(calculator.division(a, b))
else:
    print("Incorrect value!")
