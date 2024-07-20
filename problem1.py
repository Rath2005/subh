#Program to create an abstract class employee with an abstractmethod calculate_salary

from abc import ABC, abstractmethod

# Abstract class Employee

class Employee(ABC):

    @abstractmethod

    def calculate_salary(self):

        pass

# Manager subclass

class Manager(Employee):

    def _init_(self, base_salary, bonus):

        self.base_salary = base_salary

        self.bonus = bonus
    
    def calculate_salary(self):

        return self.base_salary + self.bonus

# Developer subclass

class Developer(Employee):

    def _init_(self, base_salary, project_count):

        self.base_salary = base_salary

        self.project_count = project_count
    
    def calculate_salary(self):

        # Assume a fixed amount of 500 per project

        return self.base_salary + (self.project_count * 500)

# Intern subclass

class Intern(Employee):

    def _init_(self, stipend):

        self.stipend = stipend
    
    def calculate_salary(self):

        return self.stipend

# Example Usage

if __name__ == "_main_":

    # Creating instances

    manager = Manager(base_salary=80000, bonus=10000)

    developer = Developer(base_salary=60000, project_count=5)

    intern = Intern(stipend=2000)
    
    # Calculating and printing salaries

    print(f"Manager's salary: ${manager.calculate_salary()}")

    print(f"Developer's salary: ${developer.calculate_salary()}")

    print(f"Intern's salary: ${intern.calculate_salary()}")