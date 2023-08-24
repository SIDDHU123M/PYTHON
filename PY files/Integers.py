import os

os.system("cls || clear")

#1. Whole numbers without decimal points.
#2. Immutable.

x = 5
y = 3
print(x + y)  # Output: 8
print(x * y)  # Output: 15
print(x / y)  # Output: 1.666...
print(int(3.7))  # Output: 3
print(bin(x))  # Output: 0b101 (binary representation)




# Arithmetic Operators:

# Arithmetic operators are used to perform basic mathematical operations on numerical values.

# 1. Addition (+): Adds two numbers.
# 2. Subtraction (-): Subtracts the right operand from the left operand.
# 3. Multiplication (*): Multiplies two numbers.
# 4. Division (/): Divides the left operand by the right operand, yielding a floating-point result.
# 5. Floor Division (//): Divides and truncates the decimal part, giving the floor value.
# 6. Modulus (%): Returns the remainder of the division.
# 7. Exponentiation (**): Raises the left operand to the power of the right operand.


x = 10
y = 3

print(x + y)  # Output: 13
print(x - y)  # Output: 7
print(x * y)  # Output: 30
print(x / y)  # Output: 3.333...
print(x // y)  # Output: 3
print(x % y)  # Output: 1
print(x ** y)  # Output: 1000



# Bitwise Operators:

# Bitwise operators are used to manipulate individual bits of integers. They are often used in low-level programming and to perform certain optimizations.

# 1. Bitwise AND (&): Performs a bitwise AND operation on each corresponding bit of the operands.
# 2. Bitwise OR (|): Performs a bitwise OR operation on each corresponding bit of the operands.
# 3. Bitwise XOR (^): Performs a bitwise XOR (exclusive OR) operation on each corresponding bit of the operands.
# 4. Bitwise NOT (~): Inverts the bits of the operand.
# 5. Left Shift (<<): Shifts the bits of the left operand to the left by the number of positions specified by the right operand.
# 6. Right Shift (>>): Shifts the bits of the left operand to the right by the number of positions specified by the right operand.

x = 10  # 1010 in binary
y = 3   # 0011 in binary

print(x & y)   # Output: 2 (0010 in binary)
print(x | y)   # Output: 11 (1011 in binary)
print(x ^ y)   # Output: 9 (1001 in binary)
print(~x)      # Output: -11 (1111 1111 1111 1111 1111 1111 1111 0101 in binary, due to two's complement representation)
print(x << 2)   # Output: 40 (101000 in binary, shifted 2 positions to the left)
print(x >> 1)   # Output: 5 (0101 in binary, shifted 1 position to the right)
