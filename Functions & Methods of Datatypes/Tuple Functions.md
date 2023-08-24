**Tuple Data Type:**




**Characteristics:**

- An ordered collection of items enclosed in parentheses.

- Immutable: Once created, a tuple cannot be modified.




**Features:**

- Efficient for storing multiple items with different data types.

- Supports indexing and slicing like lists.

- Useful for cases where immutability and order are important.




---




**Methods of the Tuple Data Type:**




**Part 1: Access and Manipulation:**

1. **Indexing (`tuple[index]`):** Access an item at the specified index.

2. **Slicing (`tuple[start:end]`):** Extract a sub-tuple from the specified range.

3. **Concatenation (`tuple + other_tuple`):** Combine two tuples.




**Part 2: Tuple Length:**

4. **`len(tuple)`:** Returns the number of items in the tuple.




**Part 3: Count and Index:**

5. **`tuple.count(item)`:** Counts the occurrences of an item in the tuple.

6. **`tuple.index(item)`:** Returns the index of the first occurrence of an item.




---




**Examples:**




**Part 1: Access and Manipulation:**

```python

my_tuple = (1, 'apple', 3.14, 'banana')




print(my_tuple[0])      # Output: 1

print(my_tuple[1:3])    # Output: ('apple', 3.14)

new_tuple = my_tuple + ('cherry', 42)

print(new_tuple)        # Output: (1, 'apple', 3.14, 'banana', 'cherry', 42)

```




**Part 2: Tuple Length:**

```python

my_tuple = (1, 2, 3, 4, 5)




length = len(my_tuple)

print(length)  # Output: 5

```




**Part 3: Count and Index:**

```python

my_tuple = (1, 2, 2, 3, 4, 2)




count_2 = my_tuple.count(2)

index_3 = my_tuple.index(3)




print(count_2)  # Output: 3

print(index_3)  # Output: 3

```



# Tuples Methods

### Count occurrences of an element
```python
my_tuple = (1, 2, 3, 2, 4)

my_tuple.count(2)

# Output: 2
```



### Find index of an element
```python
my_tuple.index(3)

# Output: 2
```



### Convert to list
```python
list_from_tuple = list(my_tuple)

# Output: [1, 2, 3, 2, 4]
```



### Convert to tuple
```python
tuple_from_list = tuple(list_from_tuple)

# Output: (1, 2, 3, 2, 4)
```



### Concatenate tuples
```python
tuple1 = (1, 2, 3)

tuple2 = (4, 5, 6)

concatenated_tuple = tuple1 + tuple2

# Output: (1, 2, 3, 4, 5, 6)
```



### Repetition of a tuple
```python
repeated_tuple = tuple1 * 2

# Output: (1, 2, 3, 1, 2, 3)
```



### Check if an element is in the tuple
```python
2 in tuple1

# Output: True
```



### Slicing
```python
tuple3 = (10, 20, 30, 40, 50)

tuple3[1:4]

# Output: (20, 30, 40)
```