"""
The Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable with objects of its subclasses without affecting the correctness of the program.
In simpler terms, if a class is a subclass of another class, it should be able to be used interchangeably with its parent class.
"""


# Here are a few examples to illustrate the Liskov Substitution Principle:

# Example 1: Violation of LSP
class Bird:
    def fly(self):
        pass


class Ostrich(Bird):
    def fly(self):
        # Ostriches can't fly, so this method violates LSP
        raise Exception("Ostrich can't fly")


# In this example, the Ostrich class is a subclass of Bird, but it doesn’t adhere to LSP because it raises an exception when the fly method is called.
# Example 2: Applying LSP

class Bird:
    def move(self):
        pass


class Ostrich(Bird):
    def move(self):
        # Ostriches run instead of flying
        pass


# In this improved version, the Ostrich class overrides the move method to accurately represent its behavior, adhering to LSP.
# Example 3: Using Shape Hierarchy

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        # Calculate circle area
        pass


class Rectangle(Shape):
    def area(self):
        # Calculate rectangle area
        pass

"""
In this example, the Circle and Rectangle classes can be substituted for the Shape class, 
demonstrating the LSP. You can replace instances of Shape with instances of its subclasses without affecting the behavior of the program.
"""

"""
By following the Liskov Substitution Principle, 
you ensure that your codebase remains consistent and that you can use polymorphism effectively without unexpected issues arising when substituting subclass instances for superclass instances.
"""