def enough(cap, on, wait):
    """
    This function determines
    if there is enough space
    for all passengers on the bus.
    """

    not_passengers = wait - (cap - on)
    if not_passengers <= 0:
        return 0
    else:
        return not_passengers
