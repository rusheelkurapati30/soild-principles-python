# The Single Responsibility Principle(SRP) states that a class should have only one reason to change,
# meaning it should have only one responsibility.In Python,
# this principle encourages you to create classes that have a single, well-defined purpose.

# Example1: Violation of SRP
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def calculate_salary(self):
        # Calculate the employee's salary
        pass

    def save_to_database(self):
        # Save employee data to the database
        pass


# In this example, the Employee class violates SRP because it has two distinct responsibilities:
#  calculating salary and saving data to the database.

# Example2: Applying SRP
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def calculate_salary(self):
        # Calculate the employee's salary
        pass


class DatabaseManager:
    def save_to_database(self, employee):
        # Save employee data to the database
        pass


# In this improved version, the Employee
# class focuses solely on representing an employee and calculating salary.
# The responsibility of saving data to the database is delegated to the DatabaseManager class.

# Example 3: More Focused Classes

class SalaryCalculator:
    def calculate_salary(self, employee):
        # Calculate the employee's salary
        pass


class EmployeeDatabase:
    def save_to_database(self, employee):
        # Save employee data to the database
        pass

# In this example, the responsibilities are even more clearly separated.The SalaryCalculator
# class handles salary calculations, while the EmployeeDatabase class manages database interactions.
# By adhering to SRP, your code becomes more modular, easier to understand, and simpler to modify since changes in one responsibility won’t affect the others.
