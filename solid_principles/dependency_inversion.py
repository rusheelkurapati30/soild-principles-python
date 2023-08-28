"""
The Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules;
both should depend on abstractions. Additionally, abstractions should not depend on details;
details should depend on abstractions.
In essence, DIP encourages decoupling between components by promoting the use of interfaces or abstract classes to define contracts between them.

Here are a few examples to help explain the Dependency Inversion Principle:
"""

# Example1: Violation of DIP


class LightBulb:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Switch:
    def __init__(self, bulb):
        self.bulb = bulb

    def operate(self):
        self.bulb.turn_on()


# In this example,
# the Switch class directly depends on the concrete implementation of LightBulb,
# violating DIP. If you wanted to use a different type of light source, you’d need to modify the Switch class.

# Example2: Applying DIP

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()


"""
In this improved version, the Switch class depends on the Switchable interface (abstraction) rather than the concrete LightBulb class. 
This adheres to DIP, allowing you to easily swap out different implementations of Switchable without modifying the Switch class.
"""

# Example3: High - Level and Low - Level Modules


class EmailSender:
    def send_email(self, recipient, message):
        pass


class NotificationService:
    def __init__(self, sender):
        self.sender = sender

    def send_notification(self, recipient, message):
        self.sender.send_email(recipient, message)


"""
In this scenario, the NotificationService depends on the concrete EmailSender, violating DIP. 
Instead, you could use an interface like NotificationSender and implement it for various notification methods.
"""

"""
By adhering to the Dependency Inversion Principle, you create a more flexible and maintainable architecture where high-level modules are shielded from the details of low-level modules, 
promoting modular design and easier component replacement.
"""