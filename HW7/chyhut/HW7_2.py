import re


def validity_of_password():
    password = input("Enter your password: ")
    a = True
    while a:
        if len(password) < 6 or len(password) > 16:
            break
        elif not re.search('[a-z]', password):
            break
        elif not re.search('[A-Z]', password):
            break
        elif not re.search('[0-9)]', password):
            break
        elif not re.search('[$#@]', password):
            break
        else:
            return "Valid Password"

    while a:
        return "Not a Valid Password"


w = validity_of_password()
print(w)
