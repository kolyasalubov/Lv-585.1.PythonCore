def create_array(n: int) -> list:
    """
    Creates a list of numbers from 1 to n inclusive

    Parameters
    ----------
    n: The last element of created array

    Returns
    -------
    list: a list of integers from 1 to n inclusive
    """
    res=[]
    for i in range(1,n+1): 
        res+=[i]
    return res