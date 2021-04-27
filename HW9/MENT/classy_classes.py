class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = "{0}s age is {1}".format(self.name, self.age)

        def getInfo(self):
            return self.info