import HW7_mod

figure = input("1 - rectangle, 2 - triangle, 3 - circle: ")
if figure == '1':
    print (HW7_mod.return_rectangle_square())
elif figure == '2':
    print (HW7_mod.return_triangle_square())
elif figure == '3':
    print (HW7_mod.return_circle_square())
else:
    print ("Your choice is incorrect")