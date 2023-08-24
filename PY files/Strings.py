import os

os.system("cls || clear")

# Sequence of characters enclosed in quotes.
# Immutable, meaning they can't be changed after creation.


message = "Hello, World!"

print(len(message))  # Output: 13
print(message[0])    # Output: H
print(message[7:12])  # Output: World
print(message.upper())  # Output: HELLO, WORLD!
print(message.replace("World", "Python"))  # Output: Hello, Python!
print(message.split(","))  # Output: ['Hello', ' World!']


# Length of a string
len("hello")  # Output: 5

# Concatenate strings
"hello" + " " + "world"  # Output: 'hello world'

# Accessing characters by index
"hello"[1]  # Output: 'e'

# Slicing a string
"hello"[1:4]  # Output: 'ell'
"hello"[:3]   # Output: 'hel'
"hello"[2:]   # Output: 'llo'

# Checking for substring presence
"world" in "hello world"  # Output: True

# Finding substring index
"hello world".index("world")  # Output: 6

# Changing case
"Hello".lower()  # Output: 'hello'
"world".upper()  # Output: 'WORLD'

# Replacing substring
"hello world".replace("world", "there")  # Output: 'hello there'

# Stripping whitespace
"   hello   ".strip()  # Output: 'hello'

# Splitting into a list
"hello world".split()  # Output: ['hello', 'world']

# Joining a list into a string
"-".join(["hello", "world"])  # Output: 'hello-world'

# Checking if a string starts/ends with a substring
"hello world".startswith("hello")  # Output: True
"hello world".endswith("world")    # Output: True

# Formatting strings
"{} is {}".format("Apple", "fruit")  # Output: 'Apple is fruit'

# Removing specified characters from the beginning/end
"$$$price$$".lstrip("$")  # Output: 'price$$'
"price$$$".rstrip("$")    # Output: 'price'