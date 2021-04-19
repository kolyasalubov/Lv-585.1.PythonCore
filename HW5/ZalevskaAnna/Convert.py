def bool_to_word(boolean):
    if boolean == True:
        boolean = str(boolean)
        boolean = "Yes"
        return boolean
    if boolean == False:
        boolean = str(boolean)
        boolean = "No"
        return boolean    

print(bool_to_word(True))