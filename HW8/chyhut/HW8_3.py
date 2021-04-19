class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def info_emp(self):
        return f"It is {self.name}, salary: {self.salary}."

    @staticmethod
    def count_emp():
        return f"Number of employees:{Employee.count}."


emp1 = Employee("Olha", 7850)
emp2 = Employee("Vira", 14096)
Employee.count_emp()
emp1.info_emp()
emp2.info_emp()

print(f"__bases__:{Employee.__bases__}")
print(f"__dict__:{Employee.__dict__}")
print(f"__name__:{Employee.__name__}")
print(f"__module__:{Employee.__module__}")
print(f"__doc__:{Employee.__doc__}")

