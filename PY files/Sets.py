import os

os.system("cls || clear")

# Sets:

# Characteristics:

# Unordered collection of unique elements.
# Mutable.
# Methods and Features:

# len(): Returns the number of elements.
# Set Operations: union(), intersection(), difference(), etc.
# set.add(item): Add an item to the set.
# set.remove(item): Remove an item from the set.
# set.discard(item): Remove an item if present.

fruits = {'apple', 'banana', 'cherry'}

print(len(fruits))  # Output: 3
print('apple' in fruits)  # Output: True
print('orange' in fruits)  # Output: False

# Set Operations
citrus_fruits = {'orange', 'lemon'}

print(fruits.union(citrus_fruits))  # Output: {'banana', 'cherry', 'lemon', 'apple', 'orange'}
print(fruits.intersection(citrus_fruits))  # Output: set()
print(fruits.difference(citrus_fruits))  # Output: {'cherry', 'banana', 'apple'}

# Modifying Sets
fruits.add('kiwi')
print(fruits)  # Output: {'cherry', 'banana', 'apple', 'kiwi'}
fruits.remove('banana') # Error is key not there
print(fruits)  # Output: {'cherry', 'apple', 'kiwi'}
fruits.discard('pear')  # No error even if 'pear' is not present
print(fruits)  # Output: {'cherry', 'apple', 'kiwi'}
