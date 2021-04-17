# class Car:
#     def __init__(self, name, kind, model, status):
#         self.name = name
#         self.kind = kind
#         self.model = model
        
#     def start(self):
#          print(f"Car started {self.name}")

#     def stop(self):
#         print(f"Car stopped {self.name}")      

# my_car = Car("BMW", "sport", "m5")
# print(my_car)

# my_car.start()
# my_car.stop()


class Human:
    def __init__(self, name):
        self.name = name

    def greet(self, msg = 'Hello,'):
        print(f"{msg} {self.name}")

    @classmethod
    def info(cls):
        print("Humans are also known as 'Homosapiens'")

    @staticmethod
    def speak(msg = "Hi!"):
        print(f"Someone said: '{msg}'")


petro = Human("Petro")
petro.greet("Say 'Hi!' to")
petro.greet()
petro.speak()