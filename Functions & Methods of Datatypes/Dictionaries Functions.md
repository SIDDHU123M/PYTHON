**Dictionary (`dict`) Data Type:**


**Characteristics:**

- Represents a collection of key-value pairs enclosed in curly braces `{}`.

- Keys are unique and immutable, often strings or numbers.

- Values can be of any data type.




**Features:**

- Efficient for storing and retrieving data by keys.

- Useful for modeling relationships between items.

- Keys provide a way to quickly locate values.


---

**Methods of the Dictionary Data Type:**




**Part 1: Access and Manipulation:**

1. **Accessing Values (`dict[key]`):** Access the value associated with a key.

2. **Updating Values (`dict[key] = value`):** Update the value associated with a key.

3. **Adding Key-Value Pairs (`dict[new_key] = new_value`):** Add a new key-value pair.

4. **Deleting Key-Value Pairs (`del dict[key]`):** Remove a key-value pair by key.




**Part 2: Dictionary Length:**

5. **`len(dict)`:** Returns the number of key-value pairs in the dictionary.




**Part 3: Dictionary Methods:**

6. **`dict.keys()`:** Returns a view of all keys in the dictionary.

7. **`dict.values()`:** Returns a view of all values in the dictionary.

8. **`dict.items()`:** Returns a view of all key-value pairs in the dictionary.

9. **`dict.get(key, default)`:** Returns the value for a key, or a default value if the key is not found.

10. **`dict.pop(key, default)`:** Removes and returns the value for a key, or a default value if the key is not found.

11. **`dict.popitem()`:** Removes and returns the last key-value pair added.

12. **`dict.clear()`:** Removes all key-value pairs from the dictionary.




---

**Examples:**




**Part 1: Access and Manipulation:**

```python

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}




print(my_dict['name'])         # Output: Alice

my_dict['age'] = 26

my_dict['occupation'] = 'Engineer'

del my_dict['city']

print(my_dict)                 # Output: {'name': 'Alice', 'age': 26, 'occupation': 'Engineer'}

```




**Part 2: Dictionary Length:**

```python

my_dict = {'apple': 3, 'banana': 2, 'cherry': 5}




length = len(my_dict)

print(length)  # Output: 3

```




**Part 3: Dictionary Methods:**

```python

my_dict = {'name': 'Alice', 'age': 25, 'city': 'Wonderland'}




keys = my_dict.keys()

values = my_dict.values()

items = my_dict.items()

print(keys)    # Output: dict_keys(['name', 'age', 'city'])

print(values)  # Output: dict_values(['Alice', 25, 'Wonderland'])

print(items)   # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Wonderland')])




occupation = my_dict.get('occupation', 'Unknown')

print(occupation)  # Output: Unknown




removed_value = my_dict.pop('age', None)

print(removed_value)  # Output: 25




removed_item = my_dict.popitem()

print(removed_item)  # Output: ('city', 'Wonderland')




my_dict.clear()

print(my_dict)  # Output: {}

```

# Dictionaries Functions

### Create a dictionary
```python
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

# Access value using key

my_dict['name']

# Output: 'Alice'
```



### Get keys and values as lists
```python
keys_list = my_dict.keys()

# Output: dict_keys(['name', 'age', 'city'])

values_list = my_dict.values()

# Output: dict_values(['Alice', 30, 'New York'])
```



### Check if a key is in the dictionary
```python
'age' in my_dict

# Output: True
```



### Add or update a key-value pair
```python
my_dict['occupation'] = 'Engineer'

# Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}
```

### Remove a key-value pair
```python
my_dict.pop('age')

# Output: 30
```



### Remove and return a key-value pair
```python
my_dict.popitem()

# Output: ('occupation', 'Engineer')
```



### Copy a dictionary
```python
new_dict = my_dict.copy()

# Output: {'name': 'Alice', 'city': 'New York'}
```