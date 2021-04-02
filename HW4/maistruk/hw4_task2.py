#Write a script that will check whether the entered number is even or odd and display the appropriate message. 

# a = 56

# if a%2 == 0:
#     print ('Entered number is even')
# else:
#     print ('Entered number is odd')

#2

num = int(input("Please, eneter nember: "))

while num%2 == 0:
    print (f"Entered number {num} is even")
    break
else:
    print (f"Entered number {num} is odd ")

#3

# num = int(input("Please, eneter nember: "))

# print (f"Entered number {num} is even" if num%2 == 0 else f"Entered number {num} is odd")
