def enough(cap, on, wait):
    enough = cap - (wait + on)
    if enough >= 0:
        print (f"Avaible speace is: {enough}")
    else:
        print (f"There is no enough space: {enough}")
    
print (enough( 20, 25, 10))
