def sum_of_first(n):
    return n * (n + 1) // 2

def solution(number):
    number -= 1
    if number <= 0:
        return 0
    return 3 * sum_of_first(number // 3) + 5 * sum_of_first(number // 5) - 15 * sum_of_first(number // 15)