import re
password = input("Please enter your password: ")
res = re.findall("\$|#|@",password)
res1 = re.findall("[a-z]",password)
res2 = re.findall("[A-Z]",password)
res3 = re.findall("[0-9]",password)
res4 = re.findall("......",password)
res5 = re.findall(".................",password)
if res == []:
    print("Error")
elif res1 == []:
    print("Error")
elif res2 == []:
    print("Error")
elif res3 == []:
    print("Error")
elif res4 == []:
    print("Error")
elif res5 != []:
    print("Error")
else:
    print("The password is correct")



