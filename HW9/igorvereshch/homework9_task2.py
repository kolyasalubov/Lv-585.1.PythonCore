class Car:
    def __init__(self, name = 'Kia', kind = 'sedan', model = 'Rio'):
        self.name = name
        self.kind = kind
        self.model = model
        self.started = False

    def start(self):
        if self.started:
            print(f"Sorry, but you already drive your {self.kind}.")
        else:
            self.started = True
            print(f"Wrooom. Your {self.name} {self.model} started succesfully.")

    def stop(self):
        if not self.started:
            print(f"Sorry, but your {self.kind} is already stopped.")
        else:
            self.started = False
            print(f"Your {self.name} {self.model} stopped succesfully. That was a wild ride.")


car_1 = Car()
car_1.start()
car_1.start()
car_1.stop()
car_1.stop()
print('\n')
car_2 = Car('Ford', 'hedgeback', 'Kunga')
car_2.start()
car_2.start()
car_2.stop()
car_2.stop()