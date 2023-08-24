import os

os.system("cls || clear")

# Range:

# Characteristics:

# Represents a sequence of numbers.
# Immutable.
# Features:

# Iteration: Often used in loops to generate a sequence of numbers.
# Memory Efficiency: Consumes less memory compared to storing a list of numbers.

numbers = range(5)  # Creates a range from 0 to 4
for num in numbers:
    print(num, end=' ')  # Output: 0 1 2 3 4
print()

even_numbers = range(2, 11, 2)  # Creates a range from 2 to 10, incrementing by 2
print(list(even_numbers))  # Output: [2, 4, 6, 8, 10]
