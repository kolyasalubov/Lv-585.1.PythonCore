import re

user_password = input("Please, enter your password: ")
password = True

while user_password:
    if (len(user_password)<6 or len(user_password)>16, password):
        break
    elif not re.search (r'[A-Z]', password):
        break
    elif not re.search (r'[a-z]', password):
        break
    elif not re.search (r'\+', password):
        break
    elif not re.search (r'\d', password):
        break
    else:
        print("Incorrect password. Try again")

if user_password == password:
    print("correct")
else:
    print("Error")

