class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_department(self):
        return self.department
    
    def set_department(self, department):
        self.department = department

    def __str__(self):
        return f'{self.name} is a manager with salary {self.salary}, working in the {self.department} department'

class Engineer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def get_project(self):
        return self.project
    
    def set_project(self, project):
        self.project = project

    def __str__(self):
        return f'{self.name} is an engineer with salary {self.salary}, working on the {self.project} project'
    
class Salesperson(Employee):
    def __init__(self, name, salary, region):
        super().__init__(name, salary)
        self.region = region

    def get_region(self):
        return self.region
    
    def set_region(self, region):
        self.region = region

    def __str__(self):
        return f'{self.name} is a salesperson with salary {self.salary}, working in the {self.region} region'
    
employees = [Manager('Alice', 100000, 'HR'), Engineer('Bob', 80000, 'AI'), Salesperson('Charlie', 60000, 'North')]
for employee in employees:
    print(employee)
    if isinstance(employee, Manager):
        print(employee.get_department())
        employee.set_department('Finance')
        print(employee.get_department())
    elif isinstance(employee, Engineer):
        print(employee.get_project())
        employee.set_project('ML')
        print(employee.get_project())
    elif isinstance(employee, Salesperson):
        print(employee.get_region())
        employee.set_region('South')
        print(employee.get_region())
