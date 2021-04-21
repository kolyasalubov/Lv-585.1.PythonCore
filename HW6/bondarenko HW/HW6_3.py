def count_symbols_in_row(word):
    result = {}
    for item in word:
        if item in result:
            continue
        else:
            result.update({str(item): word.count(item)})
    return result

print(count_symbols_in_row("123"))
print(count_symbols_in_row("tratata"))
print(count_symbols_in_row("1100"))