class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)

    def inputSides(self):
        side_0 = float(input("Enter side "+str(1)+" : "))
        side_1 = float(input("Enter side "+str(2)+" : "))
        self.sides = [side_0, side_1, side_0, side_1]

    def findArea(self):
        a = self.sides[0]
        b = self.sides[1]
        area = a * b
        print('The area of the rectangle is %0.2f' %area)

r = Rectangle()
r.inputSides()
r.dispSides()
r.findArea()