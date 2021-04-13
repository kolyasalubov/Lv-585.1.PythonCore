def filter_words(st: str) -> str:
    """
    st - function.
    Input parameter - st.
    Type of input parameter - str.
    Function returns the capitalized and properly spaced string.
    """

    new_st = ' '.join(st.split())
    return new_st.capitalize()
