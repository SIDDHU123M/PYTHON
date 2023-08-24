
**List Data Type:**


**Characteristics:**

- Represents an ordered collection of items enclosed in square brackets `[]`.

- Items can be of mixed data types.

- Lists are mutable, meaning they can be changed after creation.




**Features:**

- Dynamic sizing: Lists can grow or shrink in size.

- Supports indexing and slicing to access elements.

- Commonly used for storing and manipulating data.



---
**Methods of the List Data Type:**




**Part 1: Access and Manipulation:**

1. **Indexing (`list[index]`):** Access an item at the specified index.

2. **Slicing (`list[start:end]`):** Extract a sub-list from the specified range.

3. **Updating Values (`list[index] = new_value`):** Modify the value at a specific index.

4. **Appending (`list.append(item)`):** Add an item to the end of the list.

5. **Inserting (`list.insert(index, item)`):** Insert an item at a specific index.

6. **Removing (`list.remove(item)`):** Remove the first occurrence of an item.

7. **Popping (`list.pop(index)`):** Remove and return an item at a specific index.

8. **Deleting (`del list[index]`):** Delete an item at a specific index.




**Part 2: List Length:**

9. **`len(list)`:** Returns the number of items in the list.




**Part 3: List Methods:**

10. **`list.sort()`:** Sorts the list in ascending order.

11. **`list.reverse()`:** Reverses the order of items in the list.

12. **`list.copy()`:** Creates a shallow copy of the list.

13. **`list.clear()`:** Removes all items from the list.

14. **`list.extend(iterable)`:** Appends elements from an iterable to the list.

15. **`list.index(item)`:** Returns the index of the first occurrence of an item.

16. **`list.count(item)`:** Counts the occurrences of an item in the list.




---




**Examples:**




**Part 1: Access and Manipulation:**

```python

my_list = [1, 'apple', 3.14, 'banana']




print(my_list[0])          # Output: 1

print(my_list[1:3])        # Output: ['apple', 3.14]

my_list[2] = 'cherry'

my_list.append('grape')

my_list.insert(1, 'orange')

my_list.remove('apple')

popped_item = my_list.pop(2)

del my_list[0]

print(my_list)             # Output: ['orange', 3.14, 'grape']

print(popped_item)         # Output: 3.14

```




**Part 2: List Length:**

```python

my_list = [1, 2, 3, 4, 5]




length = len(my_list)

print(length)  # Output: 5

```




**Part 3: List Methods:**

```python

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]




numbers.sort()

print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]




numbers.reverse()

print(numbers)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]




numbers_copy = numbers.copy()

numbers.clear()

print(numbers)  # Output: []

print(numbers_copy)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]




numbers.extend([7, 8])

print(numbers)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1, 7, 8]




index_of_5 = numbers.index(5)

count_of_5 = numbers.count(5)

print(index_of_5)  # Output: 2

print(count_of_5)  # Output: 3

```


# Lists Functions

### Adding elements
```python
my_list = [1, 2, 3]

my_list.append(4)

# Output: [1, 2, 3, 4]
```



### Extending with another list
```python
my_list.extend([5, 6])

# Output: [1, 2, 3, 4, 5, 6]
```



### Inserting element at specific index
```python
my_list.insert(2, 2.5)

# Output: [1, 2, 2.5, 3, 4, 5, 6]
```



### Removing specific element
```python
my_list.remove(3)

# Output: [1, 2, 2.5, 4, 5, 6]
```



### Removing element at specific index
```python
my_list.pop(4)

# Output: [1, 2, 2.5, 4, 6]
```



### Finding index of element
```python
my_list.index(2.5)

# Output: 2
```



### Counting occurrences of element
```python
my_list.count(2)

# Output: 1
```



### Reversing the list
```python
my_list.reverse()

# Output: [6, 4, 2.5, 2, 1]
```



### Sorting the list
```python
my_list.sort()

# Output: [1, 2, 2.5, 4, 6]
```



### Slicing
```python
my_list[1:4]

# Output: [2, 2.5, 4]
```



### Copying the list
```python
new_list = my_list.copy()

# Output: [1, 2, 2.5, 4, 6]

```