def correct_tail(body, tail):  #creating function with two parameters
    b = body[-1:].lower()      # assining meaning to b and defining by key that last letter in a body
    c = tail[0].lower()         # assining meaning to c and by key first letter
    if b == c:                 # creating condition that if b matches c than return true
        return True
    else:
        return False
correct_tail("Fox", "x")