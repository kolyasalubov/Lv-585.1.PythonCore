def area(name):
     if name == "square":

          s = int(input("Enter square side length: "))
          sqt_area = s * s
          print(f"The are of sqaure is {sqt_area}.")

     elif name == "rectangle":

          a = int(input("Enter rectangle's height: "))
          b = int(input("Enter recntagle's breadth: "))
          rec_area = a * b
          print(f"The rectangle's square is {rec_area}.")
     
     elif name == "triangle":

          a = int(input("Enter triangle's height: "))
          b = int(input("Enter triangle's breadth: "))
          tri_area = 0.5 * b * a
          print(f"The area of triangle is {tri_area}.")

area("triangle")