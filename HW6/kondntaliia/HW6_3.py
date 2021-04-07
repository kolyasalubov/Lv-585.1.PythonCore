def characters_number(user_string):
    """
    characters_number - function
    Input parameter - string given by user
    Input parameter type - str
    Function returns the number of characters included in a given string
    """

    characters_dict = {}
    for character in user_string:
        keys = characters_dict.keys()
        if character in keys:
            characters_dict[character] += 1
        else:
            characters_dict[character] = 1
    return characters_dict
print(characters_number(input("Enter your string: ")))
