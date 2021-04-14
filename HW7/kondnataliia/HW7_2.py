import re

password = input("Please give me a password: ")
pattern = re.compile(r"(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])[A-Za-z0-9$#@]{6,16}")
result = pattern.search(password)

if result:
   print("Valid Password")
else:
   print("Invalid Password")
