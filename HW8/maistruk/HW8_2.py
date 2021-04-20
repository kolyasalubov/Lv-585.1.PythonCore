class Car:
    def __init__(self, name = 'Nissan', kind = 'SUV', model = 'RMX'):
        self.name = name
        self.kind = kind
        self.model = model

    def __str__ (self):
        return f"{self.name}, {self.kind}, {self.model}"

    def method1 (self):
        print (f"Car {self.name},{self.kind},{self.model} is stopped. ")

    def method2 (self):
        print (f"Car {self.name}, {self.kind},{self.model} started. ")



