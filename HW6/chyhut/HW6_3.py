def count_of_symbols(word):
    result = {}
    for item in word:
        if item in result:
            continue
        else:
            result.update({str(item): word.count(item)})
    return result


a = count_of_symbols("qwwertyyuui")
