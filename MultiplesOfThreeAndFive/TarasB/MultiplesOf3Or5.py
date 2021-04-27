

def solution(number):
    count_of_multiples = 0
    for x in range(0, number):
        if x % 3 == 0 or x % 5 == 0:
            count_of_multiples = count_of_multiples + x
    return count_of_multiples

