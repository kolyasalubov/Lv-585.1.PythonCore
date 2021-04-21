import math

def distance(x1: float, y1: float, x2: float, y2:float) -> float:
    """
    Calculates the distance between two points (x1, y1) and (x2, y2) rounded to 2 spaces

    Parameters
    ----------
    x1: x-coordinate of first point\n
    y1: y-coordinate of first point\n
    x2: x-coordinate of second point\n
    y2: y-coordinate of second point\n
    
    Returns
    -------
    float: Distance between points (x1, y1) and (x2, y2) rounded to 2 spaces
    """
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) , 2)

print(distance.__doc__)