def filter_words(st: str) -> str:
    """
    Returns a capitalized string with unnecessary whitespaces removed

    Parameters
    ----------
    st: string that requires capitalizing

    Returns
    -------
    str: capitalized string with unnecessary whitespaces removed
    """
    st_list = st.split()
    result = " ".join(st_list)
    return result.capitalize()