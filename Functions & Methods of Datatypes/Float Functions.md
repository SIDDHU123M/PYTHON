**Float Data Type:**




**Characteristics:**

- Represents decimal numbers.

- Limited precision due to binary representation.




**Features:**

- Supports basic arithmetic operations.

- Conversion between data types.

- Special floating-point values like infinity and NaN.

---

**Methods of the Float Data Type:**




**Part 1: Basic Arithmetic Operations:**

1. **Addition (`+`):** Adds two floating-point numbers.

2. **Subtraction (`-`):** Subtracts the right operand from the left operand.

3. **Multiplication (`*`):** Multiplies two floating-point numbers.

4. **Division (`/`):** Divides the left operand by the right operand.

5. **Exponentiation (`**`):** Raises the left operand to the power of the right operand.




**Part 2: Precision and Rounding:**

6. **`float.is_integer()`:** Returns `True` if the float is an integer, otherwise `False`.

7. **`float.as_integer_ratio()`:** Returns the numerator and denominator as a tuple.

8. **`round(float, ndigits)`:** Rounds the float to the specified number of digits.




**Part 3: Converting Between Data Types:**

9. **`int(float)`:** Converts a float to an integer by truncating the decimal part.

10. **`str(float)`:** Converts a float to a string representation.




**Part 4: Special Floating-Point Values:**

11. **Positive Infinity (`float('inf')`):** Represents positive infinity.

12. **Negative Infinity (`float('-inf')`):** Represents negative infinity.

13. **Not a Number (`float('nan')`):** Represents a value that is not a valid number.




---

**Examples:**

**Part 1: Basic Arithmetic Operations:**

```python

x = 5.0

y = 2.5




add_result = x + y

subtract_result = x - y

multiply_result = x * y

divide_result = x / y

exponentiation_result = x ** y




print(add_result)         # Output: 7.5

print(subtract_result)    # Output: 2.5

print(multiply_result)    # Output: 12.5

print(divide_result)      # Output: 2.0

print(exponentiation_result)  # Output: 55.90169943749474

```




**Part 2: Precision and Rounding:**

```python

a = 0.1 + 0.1 + 0.1

b = 0.3




print(a.is_integer())  # Output: False

print(b.is_integer())  # Output: False




numerator, denominator = a.as_integer_ratio()

print(numerator, denominator)  # Output: 3 10




rounded_a = round(a, 1)

rounded_b = round(b, 1)

print(rounded_a == rounded_b)  # Output: True

```




**Part 3: Converting Between Data Types:**

```python

float_number = 5.7




integer_part = int(float_number)

string_representation = str(float_number)




print(integer_part)           # Output: 5

print(string_representation)  # Output: 5.7

```




**Part 4: Special Floating-Point Values:**

```python

positive_infinity = float('inf')

negative_infinity = float('-inf')

not_a_number = float('nan')




print(positive_infinity)  # Output: inf

print(negative_infinity)  # Output: -inf

print(not_a_number)       # Output: nan

```

# Float Functions

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