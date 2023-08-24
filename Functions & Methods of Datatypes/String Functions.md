**String Data Type:**


**Characteristics:**

- A sequence of characters enclosed in single (`' '`) or double (`" "`) quotes.

- Immutable: Once created, a string cannot be changed in place.




**Features:**

- Concatenation: Combine strings using the `+` operator.

- Indexing and Slicing: Access individual characters or substrings using indices.

- String Methods: Built-in methods for operations like `upper()`, `lower()`, `split()`, etc.

- Formatting: String formatting using `%` operator or f-strings.




---




**Methods of the String Data Type:**




**Part 1: Access and Manipulation:**

1. **Indexing (`str[index]`):** Access a character at the specified index.

2. **Slicing (`str[start:end]`):** Extract a substring from the specified range.

3. **Concatenation (`str + other_str`):** Combine two strings.




**Part 2: String Length:**

4. **`len(str)`:** Returns the length (number of characters) of the string.




**Part 3: Case Transformation:**

5. **`str.lower()`:** Returns a new string in lowercase.

6. **`str.upper()`:** Returns a new string in uppercase.

7. **`str.capitalize()`:** Returns a new string with the first character capitalized.

8. **`str.title()`:** Returns a new string with the first character of each word capitalized.




**Part 4: Search and Replace:**

9. **`str.find(substring)`:** Returns the index of the first occurrence of the substring.

10. **`str.replace(old, new)`:** Replaces occurrences of a substring with another substring.

11. **`str.count(substring)`:** Counts the occurrences of a substring in the string.




**Part 5: Splitting and Joining:**

12. **`str.split(separator)`:** Splits the string into a list of substrings using the specified separator.

13. **`str.join(iterable)`:** Joins the elements of an iterable using the string as a separator.




**Part 6: Stripping Whitespace:**

14. **`str.strip()`:** Removes leading and trailing whitespace.

15. **`str.lstrip()`:** Removes leading whitespace.

16. **`str.rstrip()`:** Removes trailing whitespace.




**Part 7: Check and Replace Characters:**

17. **`str.startswith(prefix)`:** Checks if the string starts with the specified prefix.

18. **`str.endswith(suffix)`:** Checks if the string ends with the specified suffix.




**Part 8: Formatting:**

19. **String Formatting with `%`:** Replace placeholders with values.

20. **F-strings (`f"..."`):** Embed expressions within strings for formatting.




**Part 9: Miscellaneous:**

21. **`str.isalpha()`:** Returns `True` if all characters are alphabetic.

22. **`str.isdigit()`:** Returns `True` if all characters are digits.

23. **`str.isalnum()`:** Returns `True` if all characters are alphanumeric.

24. **`str.isspace()`:** Returns `True` if all characters are whitespace.



# String Functions

### Length of a string
```python
len("hello")  # Output: 5
```

### Concatenate strings
```python
"hello" + " " + "world"  ### Output: 'hello world'
```

### Accessing characters by index
```python
"hello"[1]  # Output: 'e'
```

### Slicing a string
```python
"hello"[1:4]  # Output: 'ell'

"hello"[:3]   # Output: 'hel'

"hello"[2:]   # Output: 'llo'
```

### Checking for substring presence
```python
"world" in "hello world"  # Output: True
```

### Finding substring index
```python
"hello world".index("world")  # Output: 6
```

### Changing case
```python
"Hello".lower()  # Output: 'hello'

"world".upper()  # Output: 'WORLD'
```

### Replacing substring
```python
"hello world".replace("world", "there")  # Output: 'hello there'
```

### Stripping whitespace
```python
"   hello   ".strip()  # Output: 'hello'
```

### Splitting into a list
```python
"hello world".split()  # Output: ['hello', 'world']
```

### Joining a list into a string
```python
"-".join(["hello", "world"])  # Output: 'hello-world'
```

### Checking if a string starts/ends with a substring
```python
"hello world".startswith("hello")  # Output: True

"hello world".endswith("world")    # Output: True
```

### Formatting strings
```python
"{} is {}".format("Apple", "fruit")  # Output: 'Apple is fruit'
```

### Removing specified characters from the beginning/end
```python
"$$$price$$".lstrip("$")  # Output: 'price$$'

"price$$$".rstrip("$")    # Output: 'price'

```
