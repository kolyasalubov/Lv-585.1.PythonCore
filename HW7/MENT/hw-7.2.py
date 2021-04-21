import re


password = input(" Enter your password: ")

def password_verification():
    result = re.compile("r(?=.*[$#@])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=^.{6,16}$)")
    if re.search(result, password):
        print("valid")
    else:
        print("invalid")

password_verification()