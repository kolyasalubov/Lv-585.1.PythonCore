n = int(input("enter the number: "))
fib = [0,1]
if n>2:
	for i in range(2, n):
		nextElement = fib[i-1] + fib[i-2]
		fib.appe7nd(nextElement)

print(fib)