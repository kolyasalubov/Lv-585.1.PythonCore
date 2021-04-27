numb_divided_by_two = []
numb_divided_by_three = []
undivided_numb = [] # creation of the empty lists

for i in range (1, 11):  # creation number i in range to 10

    if i % 3 == 0:  # condition that if numbers in range divided without remainder
        numb_divided_by_three.append(i)   # that those numbers should be added to this list
    elif i % 2 == 0:
            numb_divided_by_two.append(i)
    else:
            undivided_numb.append(i)

print(numb_divided_by_two)
print(numb_divided_by_three)
print(undivided_numb)