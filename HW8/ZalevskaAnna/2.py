class Human:
    def __init__(self, name):
        self.name = name
    def welcome(self):
        return f"{self.name}, hello"
    @classmethod
    def species(cls):
        cls.species = "Homosapiens"
        return cls.species
    @staticmethod
    def message():
        return "Hello world"
Man = Human("Name")
print(Man.welcome())
print(Human.species())
print(Human.message())