fib1 = fib2 = 1
 
n = input("Fibonacci series element number: ")
n = int(n) - 2
 
while n > 0:
    fib1, fib2 = fib2, fib1 + fib2
    n -= 1
 
print("The value of this element:", fib2)

# У верхньому варіанті ми можемо вичислити будь-яке число з ряду Фібоначчі


#а тут просто підставляємо число в дужках в останньому рядку

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
 
 
print(fibonacci(13))