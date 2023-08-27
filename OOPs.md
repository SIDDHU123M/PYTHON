**Object-Oriented Programming (OOP)**

1. **Class Definition**
   - Define a blueprint for creating objects.
   - Encapsulate data (attributes) and functionality (methods).
   
2. **Creating Objects**
   - Instantiate objects using the class constructor.
   - Access attributes and call methods using object notation.
   
3. **Inheritance**
   - Create a new class based on an existing class.
   - Inherited class (subclass) inherits attributes and methods.
   
4. **Polymorphism**
   - Different classes can be treated as instances of the same class.
   - Enables flexibility and reusability.
   
5. **Encapsulation**
   - Hide internal details and expose necessary interfaces.
   - Access attributes and methods using getters and setters.
   
6. **Constructors and Destructors**
   - `__init__` method initializes object attributes.
   - `__del__` method performs cleanup when object is deleted.
   
7. **Class Attributes and Methods**
   - Class-level attributes are shared by all instances.
   - Class methods operate on class-level attributes.
   
8. **Static Methods**
   - Defined within a class, but do not operate on class or instance attributes.
   - Used for utility functions that are related to the class.

9. **Encapsulation and super keyword**
   - Hide internal details and expose necessary interfaces.
   - Use `super()` to call methods from the superclass.

**Notes and Tips:**
- OOP focuses on creating reusable, modular, and organized code.
- Classes represent real-world entities or abstract concepts.
- Objects are instances of classes, each with its own state and behavior.
- Inheritance allows creating specialized classes based on existing ones.
- Encapsulation ensures data privacy and controlled access.
- Constructors initialize object attributes.
- Destructors perform cleanup when objects are deleted.
- Static methods are independent of class and instance attributes.
- The `super()` keyword calls methods from the superclass.
- Method overriding allows customizing behavior in subclass

**Instructions:**
- Identify entities or concepts that can be represented as classes.
- Design classes with appropriate attributes and methods.
- Utilize inheritance to create specialized classes.
- Apply encapsulation to control access to attributes.
- Use constructors to initialize object attributes.
- Implement destructors for necessary cleanup.
- Leverage class-level attributes and methods when needed.
- Use static methods for utility functions related to the class.
- Use `super()` to access methods from the superclass.
- Implement method overriding to provide specific behavior.
- Leverage polymorphism to treat different objects uniformly.


---
**Code:**

```python
# Class Definition
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        return f"{self.name} says Woof!"

# Creating Objects
my_dog = Dog("Buddy", 3)
dog_name = my_dog.name
dog_age = my_dog.age
dog_sound = my_dog.bark()

# Inheritance
class GoldenRetriever(Dog):
    def fetch(self):
        return f"{self.name} fetches the ball!"

# Polymorphism
class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

def animal_sounds(animal):
    return animal.make_sound()

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

# Constructors and Destructors
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def __del__(self):
        print(f"The {self.make} {self.model} is being removed.")

# Class Attributes and Methods
class Circle:
    pi = 3.14159
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return self.pi * self.radius ** 2

# Static Methods
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

# Using Classes and Objects
my_circle = Circle(5)
circle_area = my_circle.area()

result = MathUtils.add(10, 20)

# Encapsulation and super keyword
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate
```

