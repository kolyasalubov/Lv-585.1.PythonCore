class Employee:

    counter = 0

    def __init__(self, name, salary):
        Employee.counter += 1
        self.__name = name
        self.__salary = salary

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == " ":
            print("Can't be empty!")
        else:
            self.__name = name
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def name(self, salary):
        if salary < 0:
            print("Salary cannot be negative.")
        elif salary > 10000:
            print("Salary cannot be so high.")
        else:
            self.__salary = salary

    @staticmethod
    def employeeCounter():
        print(f"The total number of employees is {Employee.counter}.")
    
    def employeeInfo(self):
        print(f"{__class__.__name__}'s name is {self.__name}. This {__class__.__name__}'s salary is $ {self.__salary}.")

first_employee = Employee("Ivan", 3000)
second_employee = Employee("Inna", 5100)
third_employee = Employee("Irina", 6200)

Employee.employeeCounter()
first_employee.employeeInfo()
second_employee.employeeInfo()
third_employee.employeeInfo()
print(f"The basic classes from which the Employee class is inherited: {Employee.__bases__}.")
print(f"Information about the class namespace: {Employee.__dict__}.")
print(f"The class name is {Employee.__name__}.")
print(f"The module name in which the class is defined: {Employee.__module__}.")
print(f"The information about the documentation bar: {Employee.__doc__}.")
