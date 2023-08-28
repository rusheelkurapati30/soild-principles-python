"""The Open / Closed Principle(OCP) states that software entities(classes, modules, functions, etc.) should be open
for extension but closed for modification.In other words, you should be able to add new functionality to a module without altering its existing code.
"""


# Here are a few examples to help explain the Open / Closed Principle:

# Example 1: Violation of OCP

class Shape:
    def __init__(self, type):
        self.type = type

    def area(self):
        if self.type == "circle":
            # Calculate circle area
            pass
        elif self.type == "rectangle":
            # Calculate rectangle area
            pass


# In this example, if you want to add a new shape (e.g., triangle), you would need to modify the Shape class, which violates the OCP.

# Example 2: Applying OCP
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


# In this improved version, the Shape
# class is open for extension because you can easily create new shape classes (e.g., Triangle) without modifying the existing code.

# Example 3: Using Strategy Pattern

class PaymentMethod:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        # Process credit card payment
        pass


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        # Process PayPal payment
        pass

# Here, the PaymentMethod
# class is open for extension by allowing new payment methods to be added (e.g., BitcoinPayment) without altering its code.


# The OCP promotes the use of design patterns like the Strategy Pattern, which encapsulate varying behavior behind a common interface, enabling you to add new behaviors without modifying existing code.
# This principle leads to more maintainable and flexible software systems.
