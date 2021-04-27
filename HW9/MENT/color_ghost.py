import random

class Ghost():
    def __init__(self):
        color = ["white", "yellow", "purple", "red"]
        self.color = random.choice(color)