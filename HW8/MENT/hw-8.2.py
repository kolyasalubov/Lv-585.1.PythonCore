class Human:
    species = "Homosapiens"
    def __init__(self, name):
        self.name = name

    def say(self, msg):
        return f"{msg} {self.name}"

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def nationality():
        return "Ukrainian"

man_1 = Human(name = "Alex")
print(man_1.say("Hi, I'm "))
print(man_1.get_species())
man_2 = Human(name = "Yuriy")
print(man_2.say("Hello, I'm "), "and I am", man_2.nationality())
print(man_2.name, ",", man_2.get_species())



