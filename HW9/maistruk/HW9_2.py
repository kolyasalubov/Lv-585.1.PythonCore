# day = [1 = 'Monday', 2 = 'Tuesday', 3 = 'Wendsday', 4 = 'Thursday', 5 = 'Friday', 6 = 'Saturday', 7 = 'Sunday']
# user_choice = int(input("Enter number: "))

try:
    user_choice = int(input("Enter number: "))
    day = {1:'Monday',2: 'Tuesday',3: 'Wendsday', 4: 'Thursday',5: 'Friday',6: 'Saturday', 7: 'Sunday'}
    for key in day:
        if user_choice == key:
            print(day.get(key))
    if user_choice >= 8:
        raise ValueError("There is no such number")
except ValueError as e:
    print(e)
