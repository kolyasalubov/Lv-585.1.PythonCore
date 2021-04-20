def list_animals(animals):
    list = ''
    for i in (len(animals)):
        list += str(i + 1) + '.' + animals[i] + '\n'
    return list

