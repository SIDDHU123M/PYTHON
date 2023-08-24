# Feature: Attributes are variables that store data, while methods are functions defined in a class.

# Example:

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

# Creating an object
circle1 = Circle(5)

# Accessing attribute and method
print(circle1.radius)          # Output: 5
print(circle1.calculate_area())  # Output: 78.5