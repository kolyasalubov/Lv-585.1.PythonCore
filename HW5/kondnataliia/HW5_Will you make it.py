def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    This function determines
    if you have enough fuel
    to get to the nearest pump.
    """
    
    fuel_needed = distance_to_pump / mpg
    if fuel_left >= fuel_needed:
        return True
    return False
    