def filter_words(st): 
    return st[0].upper() + st[1: len(st)].lower()

print (filter_words("HeLLo WorLd!"))