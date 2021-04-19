def enough(cap, on, wait):
    if on == cap:
        return wait
    elif (cap - on) >= wait:
        return 0
    elif (cap - on) < wait:
        return wait - (cap - on)
a = enough(10, 5, 15)
print(a)

