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