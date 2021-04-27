

String = input("Enter your string: ")
count1 = 0
count2 = 0  # both variable initialized to zero

for i in String:  # using loop to go through string
    if(i.isdigit()):   # establishing condition that variable i digit than to variable count1 add 1
        count1 = count1 + 1
    count2 = count2 + 1  # establishing that i in string than count2 receive plus 1

print(f"The number of digits is {count1}. The number of characters is {count2}")

