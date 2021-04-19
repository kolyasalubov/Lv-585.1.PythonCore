def countLetters(word):
    res = {}
    for sym in word:
        if sym in res:
            continue
        else:
            res.update({str(sym): word.count(sym)})
    return res

print(countLetters("helloworldhello"))