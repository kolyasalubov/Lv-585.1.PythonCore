try:
    user_number = int(input("Enter your number: "))
    days_of_the_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    for key in days_of_the_week:
        if user_number == key:
            print(days_of_the_week.get(key))
    if user_number >= 8:
        raise ValueError ("There is no such day of the week!")
except ValueError as e:
    print(e)
