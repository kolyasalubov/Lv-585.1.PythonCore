def double_char(str):
    """
    Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
    """
    return ''.join([w + w for w in str])

print (double_char('Hello'))