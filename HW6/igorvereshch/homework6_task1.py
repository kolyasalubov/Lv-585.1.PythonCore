def larger(number1: float, number2: float) -> float:
    """
    Calculates larger of two numbers and returns it

    Parameters
    ----------
    number1: First number to compare\n
    number2: Second number to compare

    Returns
    -------
    float: Larger of numbers number1 and number2
    """
    if number1 > number2:
        return number1
    return number2

help(larger)