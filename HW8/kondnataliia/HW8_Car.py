class Car:
    def __init__(self, kind = "Sedan", name = "Kia", model = "Ria"):
        self.kind = kind
        self.name = name
        self.model = model
    
    def __str__(self):
        return f"{self.kind} {self.name} {self.model}"

    def car_started(self):
        print(f"{self.kind} {self.name} {self.model} started.")
    
    def car_stopped(self):
        print(f"{self.kind} {self.name} {self.model} stopped.")

c = Car()
c.car_started()
c.car_stopped()

# Люба, вибач, більше не буду зловживати тими input-ами, просто хотіла вже довести почату справу до кінця ;)

class Car:
    def __init__(self, kind = "sedan", name = "Kia", model = "Ria"):
        self.kind = input("Enter the kind of your car: ")
        self.name = input("Enter the name of your car: ")
        self.model = input("Enter the model of your car: ")
        self.speed = int(input("Enter the speed of your car: "))

    def __repr__(self):
        return f"{self.kind} {self.name} {self.model}"

    def car_started(self):
        if self.speed > 0:
            print(f"{self.kind} {self.name} {self.model} started.")
    
    def car_stopped(self):
        if self.speed == 0:
           print(f"{self.kind} {self.name} {self.model} stopped.")

c = Car()
c.car_started()
c.car_stopped()
