**Boolean (`bool`) Data Type:**




**Characteristics:**

- Represents binary values: `True` or `False`.

- Used for logical operations and comparisons.


**Features:**

- Logical operators (`and`, `or`, `not`) for combining boolean values.

- Comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) for comparisons.

---

**Methods and Operators of the Boolean Data Type:**


**Part 1: Logical Operators:**

1. **`and`:** Returns `True` if both operands are `True`, otherwise `False`.

2. **`or`:** Returns `True` if at least one operand is `True`, otherwise `False`.

3. **`not`:** Returns the opposite of the operand's boolean value (`True` becomes `False` and vice versa).


**Part 2: Comparison Operators:**

4. **Equal (`==`):** Returns `True` if both operands are equal, otherwise `False`.

5. **Not Equal (`!=`):** Returns `True` if operands are not equal, otherwise `False`.

6. **Less Than (`<`):** Returns `True` if the left operand is less than the right operand, otherwise `False`.

7. **Greater Than (`>`):** Returns `True` if the left operand is greater than the right operand, otherwise `False`.

8. **Less Than or Equal (`<=`):** Returns `True` if the left operand is less than or equal to the right operand, otherwise `False`.

9. **Greater Than or Equal (`>=`):** Returns `True` if the left operand is greater than or equal to the right operand, otherwise `False`.


---

**Examples:**


**Part 1: Logical Operators:**

```python

x = True

y = False


result_and = x and y

result_or = x or y

result_not = not x


print(result_and)  # Output: False

print(result_or)   # Output: True

print(result_not)  # Output: False

```

**Part 2: Comparison Operators:**

```python

a = 10

b = 5



equal_result = a == b

not_equal_result = a != b

less_than_result = a < b

greater_than_result = a > b

less_than_equal_result = a <= b

greater_than_equal_result = a >= b




print(equal_result)            # Output: False

print(not_equal_result)        # Output: True

print(less_than_result)        # Output: False

print(greater_than_result)     # Output: True

print(less_than_equal_result)  # Output: False

print(greater_than_equal_result)  # Output: True

```

# Boolean Functions

### Absolute value
```python
abs(-3.14)  # Output: 3.14
```

### Conversion functions
```python
float(42)  # Output: 42.0
```

### Rounding functions
```python
round(3.14159, 2)  # Output: 3.14
```

### Exponential notation
```python
"{:.2e}".format(12345.6789)  # Output: '1.23e+04'
```

### Maximum and minimum
```python
max(1.5, 2.7, 0.3)  # Output: 2.7

min(1.5, 2.7, 0.3)  # Output: 0.3
```

### Summation
```python
sum([1.1, 2.2, 3.3])  # Output: 6.6
```

### Floor division
```python
7.0 // 3.0  # Output: 2.0
```

### Modulo operation
```python
7.0 % 3.0   # Output: 1.0

```