import re

def is_valid(password):
    pattern = r"(?=.*[$#@])(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=^.{6,16}$)"
    if re.search(pattern, password):
        return 'valid'
    else:
        return 'invalid'

# Just for tests
passwords = []
passwords.append("Ab3#") # Invalid because too short (4 symbols)
passwords.append("Abcd5fghi0@#$@#$##!z") # Invalid because too long (20 symbols)
passwords.append("abc3def#") # Invalid because no capital letter
passwords.append("ABC3DEF#") # Invalid because no lowercase letter
passwords.append("Abcdef7") # Invalid because no symbol $, #, or @
passwords.append("Abcdef#") # Invalid because no digits
passwords.append("Abc def3#!") # Valid, no limits on ' ' or '!' symbols are given
passwords.append("Abc3def#") # Valid, normal password
for p in passwords:
    print(f"{p} is {is_valid(p)}")