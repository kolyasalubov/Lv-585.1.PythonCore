class Employee:
    emp_count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def displayCount(self):
        return f"Total Employee {Employee.emp_count}"

    def displayEmployee(self):
        return f"Name : {self.name}, Salary: {self.salary}"

emp_1 = Employee("Sergo", 7000)
emp_2 = Employee("Tony", 10000)
emp_3 = Employee("Garik", 8000)

print(Employee.emp_count)
print(emp_1.displayCount())
print(emp_3.displayEmployee())

print(f"Employee.__doc__:{Employee.__doc__}")
print(f"Employee.__name__:{Employee.__name__}")
print(f"Employee.__module__:{Employee.__module__}")
print(f"Employee.__bases__:{Employee.__bases__}")
print(f"Employee.__dict__:{Employee.__dict__}")