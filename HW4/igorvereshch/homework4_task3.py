# range(n - 2) бо в списку вже є 2 числа, тому нам треба додати не n, а n - 2
n = int(input("Enter amount of Fibonacci numbers: "))
fibo = [0, 1]
for i in range(n - 2):
    fibo.append(fibo[i] + fibo[i + 1])
print("List of first {0} Fibonacci numbers: {1}".format(n, fibo))
