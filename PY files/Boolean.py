import os

os.system("cls || clear")

# Booleans:

# Characteristics:

# 1. Represents True or False values.
# 2. Used for logical comparisons and conditions.
# 3. Methods and Features:

# Logical Operators: and, or, not.
# Comparison Operators: ==, !=, <, >, <=, >=.

x = True
y = False
print(x and y)  # Output: False
print(x or y)   # Output: True
print(not y)    # Output: True
print(x == y)   # Output: False


# The boolean data type represents binary values, typically True or False. It's used to perform logical operations and comparisons.

# Logical Operators:

# and: Returns True if both operands are True, otherwise False.
# or: Returns True if at least one operand is True, otherwise False.
# not: Returns the opposite of the operand's boolean value (True becomes False and vice versa).
# Comparison Operators:

# Equal (==): Returns True if both operands are equal, otherwise False.
# Not Equal (!=): Returns True if operands are not equal, otherwise False.
# Less Than (<): Returns True if the left operand is less than the right operand, otherwise False.
# Greater Than (>): Returns True if the left operand is greater than the right operand, otherwise False.
# Less Than or Equal (<=): Returns True if the left operand is less than or equal to the right operand, otherwise False.
# Greater Than or Equal (>=): Returns True if the left operand is greater than or equal to the right operand, otherwise False.


# Examples:
# Logical Operators

x = True
y = False

result_and = x and y
result_or = x or y
result_not = not x

print(result_and)  # Output: False
print(result_or)   # Output: True
print(result_not)  # Output: False

# Comparison Operators: ``
a = 10
b = 5

equal_result = a == b
not_equal_result = a != b
less_than_result = a < b
greater_than_result = a > b
less_than_equal_result = a <= b
greater_than_equal_result = a >= b

print(a == b)  # Output: False
print(a != b)  # Output: True
print(a < b)   # Output: False
print(a > b)   # Output: True
print(a <= b)  # Output: False
print(a >= b)  # Output: True


# 1. In the logical operators example, x is True and y is False. So, x and y evaluates to False, x or y evaluates to True, and not x evaluates to False.
# 2. In the comparison operators example, a is 10 and b is 5. a == b is False, a != b is True, a < b is False, a > b is True, a <= b is False, and a >= b is True.
