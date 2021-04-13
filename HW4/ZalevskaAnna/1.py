num = int(input())
 
fact = 1
if num == 1 or num ==0:
    print("Factorial {}! =".format(num), fact)
elif num < 0:
    print("Factorial non positive number don't exist")
else:
    for item in range(1, num+1):
        fact *= item
    
    print("Factorial {}! =".format(num), fact)
    
