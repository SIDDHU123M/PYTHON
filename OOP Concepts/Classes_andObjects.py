# Classes are blueprints for creating objects. They define the structure and behavior of objects.

# Example:

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking!")

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
dog2.bark()       # Output: Max is barking