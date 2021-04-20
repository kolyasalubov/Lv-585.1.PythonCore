# def solution(number):
#     number = []
#     for n in range(10):
#         if n%3 == 0 and n%5 == 0:
#             return number.append(n)
#         elif n < 0:
#             return 0
#     return sum(number)

#2

print (sum([n for n in range (1,10) if n%3 == 0 and n%5 == 0]))

