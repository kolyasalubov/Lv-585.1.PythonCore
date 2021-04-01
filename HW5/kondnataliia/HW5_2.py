login = input("Enter your login:")

while login != "First":
    login = input("Try again! \nWhat is your login?")
else:
    print(f"Hello, {login}!")
    