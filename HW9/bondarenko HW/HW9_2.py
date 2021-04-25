number = int(input("Enter your num from 1 to 7:"))
def day_of_week(num):
    try:
        if number <= 0 or number >= 8:
            raise ValueError("Bad try")
    except ValueError as e:
        print(e)
    else:
        day = {
            1: 'Monday', 
            2: 'Tuesday', 
            3: 'Wednesday', 
            4: 'Thursday',
            5: 'Friday', 
            6: 'Saturday', 
            7: 'Sunday'
            }
        return day.get(number)
print(day_of_week(number))