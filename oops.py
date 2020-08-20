
class Employee:
    def __init__(self, salary,name,role):#constructor
        self.salary=salary
        self.name=name
        self.role=role
    def printdetails(self):
        return f"Name:{self.name},Salary:{self.salary},role :{self.role}"
name1=Employee(345,"Name","programmer")
print(name1.printdetails)
#special method :__add__
class Employee1(Employee):
    def __add__(self,other):
        return self.salary+other.salary#they overload the operator
        #other operators are also used like __truediv__,
        # which are called by the print statement
#refer to mapping operators to functions
    def __repr__(self):
        return self.printdetails#this function is executed
        #every time the printfunction is executed, this is run
     #generally run with a syntax(repr)
    def __str__(self):
        #__str__is run before __repr__ for the print function
       return f"Name:{self.name},Salary:{self.salary},
        role :{self.role}"

