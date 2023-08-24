# Feature: Inheritance allows a new class (derived class or subclass) to inherit properties and behaviors from an existing class (base class or superclass).

# Example:

class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creating objects
dog = Dog()
cat = Cat()

# Calling the overridden method
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!