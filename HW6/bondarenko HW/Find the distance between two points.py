def distance(x1, y1, x2, y2):    
    import math
    return round(math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2)), 2)



#Another one



x1=int(input("enter x1 : "))

x2=int(input("enter x2 : "))

y1=int(input("enter y1 : "))

y2=int(input("enter y2 : "))

result= ((((x2 - x1 )**2) + ((y2-y1)**2)),2)

print("distance between",(x1,x2),"and",(y1,y2),"is : ",result)