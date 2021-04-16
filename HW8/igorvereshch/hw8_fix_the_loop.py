def list_animals(animals):
    list_ = ''
    for i in range(len(animals)):
        list_ += str(i + 1) + '. ' + animals[i] + '\n'
    return list_