"""A module that represents an employee"""

class Employee:
    """A class representing an employee"""

    def __init__(self, first_name, last_name, ann_salary):
        """Creates an Employee instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.ann_salary = ann_salary
    

    def give_raise(self, add_salary=50_000):
        """Gives a salary raise to an employee (defaults to $50_000)"""
        self.ann_salary += add_salary
    
    def print_employee(self):
        """Prints information about the employee"""
        full_name = f"{self.first_name.title()} + {self.last_name.title()}"
        print(f"Employee:\n-\tName: {full_name}\n-\tSalary: ${self.ann_salary}\n")
