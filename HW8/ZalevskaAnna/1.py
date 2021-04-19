class Car:
    def __init__(self, name, kind, model, status):
        self.name = name
        self.kind = kind
        self.model = model
        self.status = status
    def stoped(self):
        if self.status = "drive":
            self.status = "stop"
        return self.status
        return f"Car {self.name} stoped"
    def started(self):
        return f"Car {self.name} started"
car_1 = Car("DDD", "Sedan", "2345")
car_2 = Car("FFF", "Truck", "10000")
print(car_1)