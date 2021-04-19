DAYS_OF_WEEK = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

try:
    day_str = input("Enter a number of day of week (from 1 to 7): ")
    if day_str.lower() in DAYS_OF_WEEK:
        index = 1 + DAYS_OF_WEEK.index(day_str.lower())
        raise ValueError(f"Expected number of day of week ({index}), not it's name ({day_str}).")
    day = int(day_str)
    if day < 1 or day > 7:
        raise ValueError(f"Day must be an integer from 1 to 7, attempted {day}.")
except ValueError as e:
    print(e)
except BaseException as e:
    print("Something unexpected happened: ", e)
else:
    if day == 1:
        suffix = 'st'
    elif day == 2:
        suffix = 'nd'
    elif day == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{DAYS_OF_WEEK[day - 1].capitalize()} is {day}-{suffix} day of week.")
