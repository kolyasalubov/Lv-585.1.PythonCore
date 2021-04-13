def solution(number):
    numbers = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            numbers.append(i)
            if i < 0:
                return 0
    return sum(numbers)
print(solution(10))
