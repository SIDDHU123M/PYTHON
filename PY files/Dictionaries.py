import os
os.system("cls || clear")

# Dictionaries:

# Characteristics:

# Unordered collection of key-value pairs.
# Mutable.
# Methods and Features:

# len(): Returns the number of key-value pairs.
# Access by Key: Access values using keys.
# dict.keys(), dict.values(), dict.items(): Get keys, values, or key-value pairs.
# dict.get(key, default): Get the value for a key, with a default value if not found.
# dict.pop(key): Remove and return the value for a key.
# dict.update(other_dict): Update with key-value pairs from another dictionary.

person = {'name': 'Alice', 'age': 30, 'city': 'New York'}

print(len(person))  # Output: 3
print(person['name'])  # Output: Alice
print(person.keys())   # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(person.items())   # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
print(person.get('gender', 'Unknown'))  # Output: Unknown
print(person.pop('age'))  # Output: 30
person.update({'city': 'San Francisco', 'country': 'USA'})
print(person)  # Output: {'name': 'Alice', 'city': 'San Francisco', 'country': 'USA'}
