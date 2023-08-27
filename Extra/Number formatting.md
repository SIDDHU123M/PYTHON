**For number formatting in Python, we use the format() function. Here is an example of how you can transform numbers:**

## Number formatting with fill, alignment, sign, width, precision and type
```python 
num = 123.456789

formatted_num = format(num, "^+20.2f") 
print(formatted_num)
# The output will be: '      +123.46      '
```

**In this example:**

- `^` specifies center alignment
- `+` specifies to display the sign even for positive numbers.
- `20` is the width of the entire string.
- `.2` is the precision; the number of digits after the decimal point.
- `f` is the type; fixed point decimal notation.