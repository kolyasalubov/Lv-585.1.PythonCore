num = int(input("Enter number"))
factorial = 1
if num<1:
    print("Sorry, does not exist")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is", factorial)