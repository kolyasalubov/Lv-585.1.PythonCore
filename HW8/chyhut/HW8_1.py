class Polygon:
    def init(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: "))
                      for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print(f"Side {i + 1} is {self.sides[i]}")


class Rectangle(Polygon):
    def init(self):
        super().init(2)

    def findArea(self):
        a, b = self.sides
        s = a * b

        print(f"The area of the triangle is {s}")


t = Rectangle()