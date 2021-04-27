

def filter_words(str):  # creating function
    return str[0].upper() + str[1: len(str)].lower()  # applying to the first letter in string upper case
 # than by key and fuction len saying that we need apply lower case to the rest of string

print(filter_words("HELLO CAN YOU HEAR ME"))

