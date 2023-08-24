import os
os.system("cls || clear")

# Part 1: Conditional Statements (if, elif, else):
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# Part 2: Indentation:
if True:
    print("This is indented properly")
else:
print("This will cause an IndentationError")


# Part 3: Comparison Operators:
age = 25
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 65:
    print("You are an adult")
else:
    print("You are a senior")


# Part 4: Logical Operators:
temperature = 25
humidity = 80
if temperature > 30 or humidity > 90:
    print("It's hot and humid")
if not (temperature < 10):
    print("It's not cold")


# Part 5: Loops (for and while):
for i in range(5):
    print(i)
    
num = 0
while num < 5:
    print(num)
    num += 1


# Part 6: Range Function:
for i in range(2, 10, 2):
    print(i)  # Outputs: 2, 4, 6, 8


# Part 7: Break and Continue:
for i in range(5):
    if i == 3:
        break
    print(i)  # Outputs: 0, 1, 2
    
for i in range(5):
    if i == 2:
        continue
    print(i)  # Outputs: 0, 1, 3, 4


# Part 8: Lists and Iteration:
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)


# Part 9: Dictionaries:
student = {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}
for key, value in student.items():
    print(f"{key}: {value}")


# Part 10: Functions:
def greet(name):
    return f"Hello, {name}!"
    
message = greet("Alice")
print(message)  # Outputs: "Hello, Alice!"


# Part 11: Default and Named Arguments:
def power(base, exponent=2):
    return base ** exponent

result1 = power(2)      # 2^2 = 4
result2 = power(2, 3)   # 2^3 = 8
result3 = power(3, exponent=4)  # 3^4 = 81