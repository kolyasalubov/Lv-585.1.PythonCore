def enough(cap, on, wait):
    x = cap - on 
    if(x < wait):
      return(wait - x)
    else: 
        return(0) 

