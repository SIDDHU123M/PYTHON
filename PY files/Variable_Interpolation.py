# Variable interpolation refers to the process of embedding variables within strings to create a more readable and dynamic output. Python provides several methods for variable interpolation:


# String Concatenation:
# You can concatenate strings and variables using the + operator.
name = "Alice"
message = "Hello, " + name


# **Using % Formatting:** The %` operator can be used for basic string formatting. 
name = "Alice"
message = "Hello, %s" % name


# You can also use multiple variables:
name = "Alice"
age = 30
message = "Hello, %s! You are %d years old." % (name, age)


# Using str.format():
# The str.format() method allows more control over formatting and order of variables.
name = "Alice"
age = 30
message = "Hello, {}! You are {} years old.".format(name, age)


# You can also use positional and keyword arguments:
name = "Alice"
age = 30
message = "Hello, {0}! You are {1} years old.".format(name, age)


# f-strings (Formatted String Literals):
# Introduced in Python 3.6, f-strings are a concise and readable way to interpolate variables.
name = "Alice"
age = 30
message = f"Hello, {name}! You are {age} years old."


# You can perform expressions within f-strings:
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."


# String Template:
# The string.Template class provides a more customizable way to interpolate variables.
from string import Template

name = "Alice"
age = 30
template = Template("Hello, $name! You are $age years old.")
message = template.substitute(name=name, age=age)


# Using locals() or globals():
# You can use the locals() or globals() dictionaries to directly substitute variable names.
name = "Alice"
age = 30
message = "Hello, {name}! You are {age} years old.".format(**locals())

# Note that this approach can be risky, especially with globals(), as it might expose sensitive information.




# %s: Placeholder for inserting a string value. 
name = "Alice"
message = "Hello, %s!" % name

# %d: Placeholder for inserting an integer value.
age = 30
message = "You are %d years old." % age

# %f: Placeholder for floating-point numbers (decimal values).
name = "Alice"
age = 30
height = 1.75
message = f"Hello, {name}! You are {age} years old and {height:.2f} meters tall."

# %x: Placeholder for inserting integers as hexadecimal numbers.
# %o: Placeholder for inserting integers as octal numbers.
number = 255

hexadecimal_format = "Hexadecimal: %x" % number
octal_format = "Octal: %o" % number

print(hexadecimal_format)  # Output: Hexadecimal: ff
print(octal_format)        # Output: Octal: 377