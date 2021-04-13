def solution(number):
    countnum = []
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            countnum.append(x)
    return sum(countnum)