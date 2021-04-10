# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if not. The input values are always positive.
#1
def zero_fuel(distance_to_pump,mpg,fuel_left):
    zero_fuel = ((mpg*fuel_left)//distance_to_pump)
    if zero_fuel == 1:
        return True
    if zero_fuel != 0:
        return False

print (zero_fuel(50,25,2))

#2
# def zero_fuel(distance_to_pump,mpg,fuel_left):
#     if mpg*fuel_left >= distance_to_pump:
#         return 1
#     else:
#         return 0

# n = (zero_fuel(50, 25, 2))
# print (n)

