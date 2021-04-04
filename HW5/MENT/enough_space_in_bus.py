def enough(cap, on, wait):
    avaible_space = cap - on
    remaining = wait - avaible_space
    if remaining <= 0:
        return 0
    else:
        return remaining