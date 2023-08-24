import os
os.system("cls || clear")

# Lists:

# Characteristics:

# Ordered collection of items.
# Mutable.
# Methods and Features:

# len(): Returns the number of items.
# Indexing and Slicing: Access elements and sublists.
# list.append(item): Add an item to the end.
# list.extend(iterable): Extend with items from an iterable.
# list.insert(index, item): Insert an item at a specific index.
# list.remove(item): Remove the first occurrence of an item.
# list.pop(index): Remove and return an item at the given index.


fruits = ['apple', 'banana', 'cherry']

print(len(fruits))  # Output: 3
print(fruits[1])    # Output: banana
fruits.append('orange')
print(fruits)       # Output: ['apple', 'banana', 'cherry', 'orange']
fruits.extend(['grape', 'kiwi'])
print(fruits)       # Output: ['apple', 'banana', 'cherry', 'orange', 'grape', 'kiwi']
fruits.insert(2, 'pear')
print(fruits)       # Output: ['apple', 'banana', 'pear', 'cherry', 'orange', 'grape', 'kiwi']
fruits.remove('cherry')
print(fruits)       # Output: ['apple', 'banana', 'pear', 'orange', 'grape', 'kiwi']
print(fruits.pop(3))  # Output: orange
print(fruits)       # Output: ['apple', 'banana', 'pear', 'grape', 'kiwi']
