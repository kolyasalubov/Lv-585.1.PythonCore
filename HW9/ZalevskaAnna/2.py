num = input("Enter your number: ")
def analyz_enter_num(num):
    try:
        num = int(num)
        try:
            if num >= 8: 
                raise ValueError("The day of the week cannot be eighth or more!")
            elif num <= 0:
                raise ValueError("The day of the week cannot be negative or zero!") 
        except ValueError as e:
            print(e)
    except:
        print ("You must enter a number!")
    else:
        day_of_week = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
        return day_of_week.get(num)
print(analyz_enter_num(num))
