def insufficient_fuel(distance,mpg,fuel): # making function
    if mpg*fuel >= distance: # making condition that will define if there sufficiently fuel
        return True
    else:
        return False

our_situation = (insufficient_fuel(50, 25, 2))
print (our_situation)