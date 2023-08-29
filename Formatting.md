### String Interpolation
```python
name = "Alice"

age = 30

print(f"My name is {name} and I am {age} years old.")
```

### Formatting with .format()
```python
item = "book"

price = 15.99

print("The {} costs ${:.2f}".format(item, price))
```

### String Concatenation
```python
text1 = "Hello"

text2 = "world"

combined = text1 + " " + text2

print(combined)
```

### String Methods
```python
sentence = "   This is an example sentence.   "

print(sentence.strip())

print(sentence.lower())

print(sentence.upper())

print(sentence.replace("example", "sample"))
```

### Formatting Numbers

num = 123.45678
```python
print("Formatted: {:.2f}".format(num))

print("Formatted: {:,}".format(1000000))
```

### Alignment and Padding
```python
word = "Python"

print(f"'{word:<10}'")

print(f"'{word:^10}'")

print(f"'{word:>10}'")
```

### Truncating Long Strings
```python
long_text = "This is a very long sentence that needs to be truncated."

print(f"Truncated: '{long_text[:20]}...'")
```

### Escape Characters
```python
print("This is a line\nThis is a new line.\tThis is a tab.")
```

### Raw Strings
```python
raw_str = r"Path: C:\user\documents"

print(raw_str)
```
Formatting options that you can use with the `%` operator in Python strings. Formatting using `%` is an older formatting style in Python, and it's recommended to use the newer `.format()` method or f-strings (formatted string literals) introduced in Python 3.6. However, I'm here to provide you with the information you're seeking. Here's an overview of the formatting options using `%`:

1. **Integer Formatting:**
   - `%d`: Decimal integer.
   - `%x`: Hexadecimal integer (lowercase).
   - `%X`: Hexadecimal integer (uppercase).
   - `%o`: Octal integer.

2. **Floating-Point Formatting:**
   - `%f`: Floating-point decimal format.
   - `%e`: Floating-point exponential format (lowercase).
   - `%E`: Floating-point exponential format (uppercase).
   - `%g`: General format (chooses between `%f` and `%e`).
   - `%G`: General format (chooses between `%f` and `%E`).

3. **String Formatting:**
   - `%s`: String format (default for all types).
   - `%c`: Character format.

4. **Width and Precision:**
   - `%[width]d`, `%[width]f`, `%[width]s`: Specifies the minimum width of the output.
   - `%.[precision]f`, `%.[precision]e`: Specifies the number of decimal places for floating-point values.

5. **Alignment:**
   - `%-[width]s`: Left-aligns the string within the specified width.
   - `%+[width]d`, `%+[width]f`: Forces a plus sign for positive numbers.

6. **Signs and Fill Characters:**
   - `%+d`, `%+f`: Forces a plus sign for positive numbers.
   - `%[width]0d`, `%[width]0f`: Pads the number with zeros.

7. **Dictionary Formatting:**
   - `%(key)s`: Used in conjunction with a dictionary to insert a value based on the specified key.

Here's an example demonstrating these formatting options:

```python
integer_val = 42
float_val = 3.14159
string_val = "Hello, World!"

print("Integer: %d, Hex: %x, Octal: %o" % (integer_val, integer_val, integer_val))
print("Floating-point: %f, Exponential: %e, String: %s" % (float_val, float_val, string_val))
print("Width and Precision: %6.2f" % float_val)
print("Alignment: %-20s" % string_val)
print("Signs and Fill: %+d, %05d" % (integer_val, integer_val))
print("Dictionary: %(name)s" % {'name': 'Alice'})
```

Remember that this formatting style can become complex, especially when combining multiple formatting options. Newer formatting methods like `.format()` and f-strings provide more flexibility and readability. Feel free to explore those options if you're interested in a more modern approach to string formatting in Python!
