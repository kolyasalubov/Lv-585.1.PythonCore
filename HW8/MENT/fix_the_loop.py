def list_animals(animals: list) -> str:
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list