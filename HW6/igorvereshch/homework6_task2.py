def dict_of_chars(string):
    result = {}
    set_of_chars = set(string)
    for char in set_of_chars:
        result.update({char: string.count(char)})
    print(result)
    return result

string = "abracadabra"
dict_of_chars(string)