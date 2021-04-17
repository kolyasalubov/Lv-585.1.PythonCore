# Люба, дала нам безліч інструментів, тепер тримайся ;)
# Вибач, якщо в мене тут зайві методи. Вважай, що я їх відпрацьовую :)

class Human:
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
        return f"{self.__name}"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name == " ":
            print("Can't be empty!")
        else:
            self.__name = name

    def welcomeMessage(self):
        print(f"Welcome, {self.__name}.")

    @classmethod
    def speciesInfo(cls, species = "Homosapiens"):
        cls.species = species
        print(f"{__class__.__name__} belongs to the species {cls.species}.")
    
    @staticmethod
    def arbitraryMessage():
        print("Show must go on!")

human_1 = Human("Alex")
human_1.welcomeMessage()
Human.speciesInfo()
Human.arbitraryMessage()
