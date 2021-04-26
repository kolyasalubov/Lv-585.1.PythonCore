#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

class Ball:
    def __init__ (self, type = 'regular'):
        self.type = type

    def __str__(self):
        return f"Ball {self.type}"

    
ball1 = Ball('super')
ball2 = Ball()

print (ball1)
print (ball2)
    