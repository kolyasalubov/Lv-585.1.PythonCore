
from functools import reduce
from operator import mul
x = 3291
y = str(x)
z = int(y)

y = y[::-1]

print(reduce(mul, map(int, y)))
print(y)
print(sorted(y))
