
**Integer (`int`) Data Type:**




**Characteristics:**

- Represents whole numbers without a decimal point.

- Positive, negative, and zero values are possible.

- Supports basic arithmetic operations.




**Features:**

- Efficient for mathematical calculations.

- Precise representation of whole numbers.




---

**Methods and Operations of the Integer Data Type:**




**Part 1: Basic Arithmetic Operations:**

1. **Addition (`+`):** Adds two integers.

2. **Subtraction (`-`):** Subtracts the right operand from the left operand.

3. **Multiplication (`*`):** Multiplies two integers.

4. **Division (`/`):** Divides the left operand by the right operand.

5. **Floor Division (`//`):** Divides and rounds down to the nearest integer.

6. **Modulus (`%`):** Returns the remainder of division.

7. **Exponentiation (`**`):** Raises the left operand to the power of the right operand.




**Part 2: Converting Between Data Types:**

8. **`float(int)`:** Converts an integer to a floating-point number.

9. **`str(int)`:** Converts an integer to a string representation.




**Part 3: Comparison Operators:**

10. **Equal (`==`):** Returns `True` if both operands are equal, otherwise `False`.

11. **Not Equal (`!=`):** Returns `True` if operands are not equal, otherwise `False`.

12. **Less Than (`<`):** Returns `True` if the left operand is less than the right operand, otherwise `False`.

13. **Greater Than (`>`):** Returns `True` if the left operand is greater than the right operand, otherwise `False`.

14. **Less Than or Equal (`<=`):** Returns `True` if the left operand is less than or equal to the right operand, otherwise `False`.

15. **Greater Than or Equal (`>=`):** Returns `True` if the left operand is greater than or equal to the right operand, otherwise `False`.




---

**Examples:**




**Part 1: Basic Arithmetic Operations:**

```python

x = 10

y = 3




add_result = x + y

subtract_result = x - y

multiply_result = x * y

divide_result = x / y

floor_divide_result = x // y

modulus_result = x % y

exponentiation_result = x ** y




print(add_result)         # Output: 13

print(subtract_result)    # Output: 7

print(multiply_result)    # Output: 30

print(divide_result)      # Output: 3.333...

print(floor_divide_result)  # Output: 3

print(modulus_result)     # Output: 1

print(exponentiation_result)  # Output: 1000

```




**Part 2: Converting Between Data Types:**

```python

integer_number = 42




float_representation = float(integer_number)

string_representation = str(integer_number)




print(float_representation)  # Output: 42.0

print(string_representation)  # Output: "42"

```




**Part 3: Comparison Operators:**

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

# Integer Functions

### Absolute value
```python
abs(-5)  # Output: 5
```



### Conversion functions
```python
int(3.14)  # Output: 3
```



### Minimum and maximum
```python
min(1, 5, -3)  # Output: -3

max(1, 5, -3)  # Output: 5
```



### Rounding functions
```python
round(3.14159)  # Output: 3
```



### Exponentiation
```python
pow(2, 3)  # Output: 8
```



### Binary, octal, and hexadecimal representation
```python
bin(10)  # Output: '0b1010'

oct(10)  # Output: '0o12'

hex(10)  # Output: '0xa'
```



### Summation
```python
sum([1, 2, 3])  # Output: 6
```



### Sorting
```python
sorted([3, 1, 2])  # Output: [1, 2, 3]

```