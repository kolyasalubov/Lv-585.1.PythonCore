class Employee:
    count = 0
    def __init__(self, name, salary):
        Employee.count += 1
        self.name = name
        self.salary = salary
    def info_emp(self):
        return f"The employee {self.name} has a salary: {self.salary}"
    @staticmethod
    def total_number_emp():
        return f"The total number of employees: {Employee.count}"
    @classmethod
    def info_class(cls):
        return f"""Information about class Employee:
        The documentation bar: {cls.__doc__}
        The base classes from which the employee class is inherited: {cls.__base__}
        The class name: {cls.__name__}
        The module name in which the class is defined: {cls.__module__}
        The class namespace: {cls.__dict__}
        """
Emp1 = Employee("Ann", 10000)
Emp2 = Employee("Dan", 10000) 
print(Emp1.info_emp())
print(Emp2.info_emp())
print(Employee.total_number_emp())
print(Employee.info_class())