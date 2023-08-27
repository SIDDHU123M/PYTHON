### Printable Representation

**The `!r` in a Python f-string `(f"...")` tells Python to use the `repr()` function for the variable that it precedes. The `repr()` function returns a string containing a printable representation of an object.**

```python 
x = 'Hello, World!'
print(f"{x}")   # This will print: Hello, World!
print(f"{x!r}") # This will print: 'Hello, World!'
```

**In the second print statement, `x!r` gives us the `repr()` string representation of x, hence the single quotes around `Hello, World!` are printed as well.**