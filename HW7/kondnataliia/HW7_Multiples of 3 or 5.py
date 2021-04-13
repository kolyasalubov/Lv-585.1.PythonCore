def solution(number):
    """
    This function returns the sum of all the multiples 
    of 3 or 5 below the number passed in.
    """

    set_of_numbers = set()
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            set_of_numbers.add(i)
            if i < 0:
                return 0
    return sum(set_of_numbers)
