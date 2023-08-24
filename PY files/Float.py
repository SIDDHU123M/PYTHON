import os

os.system("cls || clear")

# Float Data Type:

# The float data type in Python represents floating-point numbers, which are numbers with a decimal point. Floats are used to represent real numbers and support a wide range of mathematical operations.

# Characteristics:

# Represents decimal numbers.
# Limited precision due to binary representation.
# Methods and Features:

# Basic arithmetic operations: +, -, *, /.
# Precision and rounding issues due to binary representation.
# Converting between data types: int(), str().
# Special floating-point values: inf (infinity), -inf (negative infinity), nan (not a number).

# Basic Arithmetic Operations
x = 5.0
y = 2.5

add_result = x + y
subtract_result = x - y
multiply_result = x * y
divide_result = x / y

print(x + y)      # Output: 7.5
print(x - y) # Output: 2.5
print(x * y) # Output: 12.5
print(x / y)   # Output: 2.0

# Precision and Rounding
a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b)  # Output: False (due to precision issues)
print(round(a, 1) == round(b, 1))  # Output: True (using rounding)

# Converting Between Data Types
integer_part = int(5.7)
string_representation = str(3.14159)

print(integer_part)           # Output: 5
print(string_representation)  # Output: 3.14159

# Special Floating-Point Values
positive_infinity = float('inf')
negative_infinity = float('-inf')
not_a_number = float('nan')

print(positive_infinity)  # Output: inf
print(negative_infinity)  # Output: -inf
print(not_a_number)       # Output: nan
