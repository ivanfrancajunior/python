'''
Employee Parsing

In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash.

Examples
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

The salary is an integer.
Check the Resources for some helpful tutorials on how to do this.

link: https://edabit.com/challenge/j2HauiSdDadkjxjsQ
'''
class Employee:
    
    def __init__(self, firstname:str=None,lastname:str=None, salary:int=None) -> None:
        self._firsname = firstname
        self._lastname = lastname
        self._salary = salary

    @property
    def firstname(self):
        return self._firsname
    
    @firstname.setter
    def firstname(self, value:str):
        if not isinstance (value, str):
            raise TypeError('The field only suport string types')   
        self._firsname = value
        
    @property
    def lastname(self):
        return self._lastname
    
    @lastname.setter
    def lastname(self, value:str):
        if not isinstance (value, str):
            raise TypeError('The field only suport string types')
        self._lastname = value
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value:int):
        self._salary = value
    
    def from_string(self, data:str) -> None: 
        
        if self.firstname == None and self.lastname == None and self.salary == None:
            new_employee_data = data.split('-')
            
            self.firstname = new_employee_data[0]
            
            self.lastname = new_employee_data[1]
            
            self.salary = int(new_employee_data[2])
        
        return 'ok'

# emp1 = Employee("Mary", "Sue", 60000)

emp1 = Employee()

print(emp1.firstname)

emp1.from_string("John-Smith-55000")

print(emp1.firstname)

# print(emp1.firstname)
    
# string = 'John-Smith-55000'
# n_string = string.split('-')
# print(n_string, type(n_string))