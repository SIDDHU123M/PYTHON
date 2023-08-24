# Feature: Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Example:

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# Creating objects
circle = Circle(5)
square = Square(4)

# Using polymorphism
shapes = [circle, square]
for shape in shapes:
    print(shape.area())