a = input("Enter a four-digit number: ")
b = int(a[0]) * int(a[1]) * int(a[2]) * int(a[3])
print('Product:', b)
a_list = list(a)
a_list.reverse()
b = "".join(a_list)
print('Reverse:', b)
a_list = list(a)
a_list.sort ()
b = "".join(a_list)
print('Sort:', b)







