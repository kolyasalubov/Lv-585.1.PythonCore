def are_you_playing_banjo(name):
    """
    The function determines 
    if the user is playing the banjo.
    """

    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
