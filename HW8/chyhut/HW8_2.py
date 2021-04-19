class Human:
    species = "Homosapiens"

    def __init__(self, name) -> None:
        self.name = name

    def greeting(self):
        return f"Welcome, {self.name}."

    @classmethod
    def InfoSpecies(cls):
        return f"It's a {cls.species}"

    @staticmethod
    def some_msg():
        return f"Smart people are the best encyclopedia"


person = Human("Olha")
person.greeting()
person.InfoSpecies()
person.some_msg()
