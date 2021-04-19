n = 5
result = 1
for i in range(n):
    result *= i + 1
print("{0}! = {1}".format(n, result))

# n той самий
N = n
result = 1
while True:
    if N == 0:
        break
    result *= N
    N -= 1
print("{0}! = {1}".format(n, result))

