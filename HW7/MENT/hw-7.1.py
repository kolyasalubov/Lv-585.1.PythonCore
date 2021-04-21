import myarea
#При виборі rectangle - "Traceback (most recent call last):"
#Буду вдячний за пояснення проблеми.

def area_of_figures():
    figures = input("Enter your figure(1 - rectangle; 2 - triangle; 3 - circle): ")
    if figures == '1':
        return myarea.area_of_rectangle()
    elif figures == '2':
        return myarea.area_of_triangle()
    elif figures == '3':
        return myarea.area_of_circle()
    else:
        return "Error! Please, enter correct name (1; 2; 3)"

print(area_of_figures())

