**Set Data Type:**

**Characteristics:**

- Represents an unordered collection of unique elements.

- Enclosed in curly braces `{}` or created using the `set()` constructor.

- Sets do not allow duplicate elements.




**Features:**

- Efficient membership testing (`in` and `not in` operations).

- Supports mathematical operations like union, intersection, and difference.

---


**Methods of the Set Data Type:**




**Part 1: Set Creation and Modification:**

1. **Creating Sets (`set(iterable)`):** Create a set from an iterable.

2. **Adding Elements (`set.add(element)`):** Add an element to the set.

3. **Updating Elements (`set.update(iterable)`):** Add multiple elements to the set.

4. **Removing Elements (`set.remove(element)`):** Remove an element from the set.

5. **Discarding Elements (`set.discard(element)`):** Remove an element if present, but do nothing if not.

6. **Popping Elements (`set.pop()`):** Remove and return an arbitrary element.

7. **Clearing (`set.clear()`):** Remove all elements from the set.




**Part 2: Set Operations:**

8. **Union (`set.union(other_set)`):** Returns a new set containing all elements from both sets.

9. **Intersection (`set.intersection(other_set)`):** Returns a new set containing common elements.

10. **Difference (`set.difference(other_set)`):** Returns a new set with elements present in the first set but not in the second.

11. **Symmetric Difference (`set.symmetric_difference(other_set)`):** Returns a new set with elements present in either set, but not in both.

12. **Subset (`set.issubset(other_set)`):** Checks if the set is a subset of another set.

13. **Superset (`set.issuperset(other_set)`):** Checks if the set is a superset of another set.




**Part 3: Set Copy and Conversion:**

14. **Copying (`set.copy()`):** Creates a shallow copy of the set.

15. **Converting to Set (`set(iterable)`):** Convert an iterable into a set.




---




**Examples:**




**Part 1: Set Creation and Modification:**

```python

my_set = {1, 2, 3}




my_set.add(4)

my_set.update([5, 6])

my_set.remove(2)

my_set.discard(7)

popped_item = my_set.pop()

my_set.clear()




print(my_set)       # Output: set()

print(popped_item)  # Output: 1

```




**Part 2: Set Operations:**

```python

set1 = {1, 2, 3}

set2 = {3, 4, 5}




union_result = set1.union(set2)

intersection_result = set1.intersection(set2)

difference_result = set1.difference(set2)

symmetric_difference_result = set1.symmetric_difference(set2)

is_subset = set1.issubset(set2)

is_superset = set1.issuperset(set2)




print(union_result)             # Output: {1, 2, 3, 4, 5}

print(intersection_result)      # Output: {3}

print(difference_result)        # Output: {1, 2}

print(symmetric_difference_result)  # Output: {1, 2, 4, 5}

print(is_subset)                # Output: False

print(is_superset)              # Output: False

```




**Part 3: Set Copy and Conversion:**

```python

original_set = {1, 2, 3}

copied_set = original_set.copy()




tuple_from_set = tuple(original_set)

list_from_set = list(original_set)




print(copied_set)          # Output: {1, 2, 3}

print(tuple_from_set)      # Output: (1, 2, 3)

print(list_from_set)       # Output: [1, 2, 3]

```


# Set Functions

### Create a set
```python
my_set = {1, 2, 3}
```



### Add an element
```python
my_set.add(4)

# Output: {1, 2, 3, 4}
```

### Remove an element
```python
my_set.remove(2)

# Output: {1, 3, 4}
```

### Check if an element is in the set
```python
2 in my_set

# Output: False
```

### Perform set operations
```python
set1 = {1, 2, 3}

set2 = {2, 3, 4}


# Union

union_set = set1 | set2

# Output: {1, 2, 3, 4}


# Intersection

intersection_set = set1 & set2

# Output: {2, 3}
```

### Difference
```python
difference_set = set1 - set2

# Output: {1}
```

### Symmetric Difference
```python
symmetric_difference_set = set1 ^ set2

# Output: {1, 4}
```

### Copy a set
```python
new_set = my_set.copy()

# Output: {1, 3, 4}
```