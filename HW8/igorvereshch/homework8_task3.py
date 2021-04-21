import re

class Employee:
    '''
    Defines information about employee: their name and salary

    Constants
    MIN_SALARY:    possible minimum of salary
    MAX_SALARY:    possible maximum of salary
    NAME_FILTER:   regex for filtering out invalid names like '12345' or 'Hi!'
    GENDER_FILTER: set for filtering out invalid genders like 'alien'

    Built-in variables
    counter: amount of hired employees

    Attributes
    name:   name of employee
    salary: salary of employee
    gender: gender of employee (only used in printing information by now)
    '''
    __MIN_SALARY = 400
    __MAX_SALARY = 2500
    __NAME_FILTER = r"^[A-Za-z]+$"
    __GENDER_FILTER = {"male", "female"}

    __counter = 0

    def __init__(self, name = "Jose", salary = 1000, gender = "male"):
        self.__name = name
        self.__salary = salary
        self.__gender = gender
        Employee.__counter += 1

    def __str__(self):
        word = "his" if self.__gender == "male" else "her"
        return f"Employee's name is {self.__name} and {word} salary is {self.__salary}"

    def __repr__(self):
        return f"Employee: name = {self.__name}, salary = {self.__salary}"

    def __del__(self):
        Employee.__counter -= 1

    def get_name(self):
        '''Returns name of an employee'''
        return self.__name

    def set_name(self, name):
        '''Changes name of an employee if entered name contains only letters, otherwise raises an error'''
        if re.match(Employee.__NAME_FILTER, name):
            self.__name = name.capitalize()
        else:
            raise ValueError(f"Name has to be a word containing of letters without whitespaces, tried '{name}'")

    name = property(get_name, set_name)

    def get_salary(self):
        '''Returns salary of an employee'''
        return self.__salary
    
    def set_salary(self, salary):
        '''
        Changes salary of an employee if salary is in between minimum and maximum possible salaries,
        otherwise raises error'''
        if not isinstance(salary, int):
            raise ValueError(f"Salary must be an integer, tried to set {type(salary)}")
        if salary >= Employee.__MIN_SALARY and salary <= Employee.__MAX_SALARY:
            self.__salary = salary
        else:
            raise ValueError(f"Salary must be in beetween {Employee.__MIN_SALARY} and {Employee.__MAX_SALARY}, "\
                           + f"tried to set {salary}")

    salary = property(get_salary, set_salary)

    def get_gender(self):
        '''Returns gender of an employee'''
        return self.__gender

    def set_gender(self, gender):
        '''Changes employee's gender if gender is valid, otherwise raises error'''
        if gender not in Employee.__GENDER_FILTER:
            raise ValueError(f"Gender must be either male or female, tried to set {gender}")
        self.__gender = gender

    gender = property(get_gender, set_gender)

    @classmethod
    def get_counter(cls):
        '''Returns amount of hired employees'''
        return Employee.__counter


if __name__ == '__main__':
    jose = Employee()

    print(jose)
    print(f"Counter after adding {jose.get_name()} as first employee: {jose.get_counter()}")

    papajohn = Employee()
    papajohn.set_name("john")
    papajohn.set_salary(1337)

    print(papajohn)
    print(f"Counter after adding {papajohn.get_name()} as second employee: {jose.get_counter()}")

    amelia = Employee()
    amelia.set_name("Amelia")
    amelia.set_salary(1500)
    amelia.set_gender("female")

    print(amelia)
    print(f"Cunter after adding {amelia.get_name()} as third employee: {Employee.get_counter()}")

    del(jose)

    print(f"Counter after firing Jose: {Employee.get_counter()}\n")

    print("__base__:", Employee.__base__)
    print("__dict__:", Employee.__dict__)
    print("__name__:", Employee.__name__)
    print("__module__:", Employee.__module__, "\n")
    print(Employee.__doc__)
    # Also __doc__ but better (imho)
    help(Employee)