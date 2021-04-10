# Create a list of integers that are entered from the terminal and determine the maximum and minimum number among them.

num_list = [int(input("Enter {} number: " .format(i+1))) for i in range (int(input("Enter amount of numbers: ")))]
print (num_list)
print (f"Maximum number is: {max(num_list)}, Minumum number is: {min(num_list)}")


