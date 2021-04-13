def count_sheeps(sheep):
    count = 0
    for x in sheep:
        if x == True:
            count += 1
    return count
            
print(count_sheeps([True, False, True, True]))