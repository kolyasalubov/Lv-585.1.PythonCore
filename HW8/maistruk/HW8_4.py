class Employee (object):
    """
    Create an employee class. Each employee 
    has characteristics such as name and salary
    """
    counter = 0

    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter +=1

    def count (self):
        print ("Total employee {}".format(Employee.counter))
    
    def hired (self):
        print (f"Name : {self.name}", ", Salary : {}".format(self.salary))

empl1 = Employee ("Jessica", 1500)
epml2 = Employee ("Monika", 3000)
empl3 = Employee ("Ania", 2000)
empl4 = Employee ("Lida", 4300)

empl1.hired()
epml2.hired()
empl3.hired()
print (Employee.counter)

print (Employee.__base__)
print (Employee.__dict__)
print (Employee.__name__)
print (Employee.__module__)
print (Employee.__doc__)