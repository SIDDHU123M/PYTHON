# **For `int`:**
# Conversion functions
int(x)
int(x, base)

# Mathematical functions
abs(x)
divmod(x, y)
pow(x, y[, z])

# Binary, octal, and hexadecimal functions
bin(x)
oct(x)
hex(x)


# **For `float`:**
# Conversion functions
float(x)

# Mathematical functions
abs(x)
pow(x, y)
round(number[, ndigits])

# Exponential notation
"{:e}".format(number)


# **For `dict`:**
# Dictionary methods
dict.fromkeys(iterable[, value])
dict.keys()
dict.values()
dict.items()
dict.get(key[, default])
dict.pop(key[, default])
dict.popitem()
dict.clear()
dict.update([other])


# **For `list`:**
# List methods
list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.index(x[, start[, end]])
list.count(x)
list.sort(key=None, reverse=False)
list.reverse()
list.copy()


# **For `set`:**
# Set methods
set.add(elem)
set.remove(elem)
set.discard(elem)
set.pop()
set.clear()
set.copy()
set.union(other, ...)
set.intersection(other, ...)
set.difference(other, ...)
set.symmetric_difference(other)
set.update(other, ...)
set.intersection_update(other, ...)
set.difference_update(other, ...)
set.symmetric_difference_update(other)
set.isdisjoint(other)
set.issubset(other)
set.issuperset(other)


# **For `str`:**
# String methods
str.capitalize()
str.casefold()
str.center(width[, fillchar])
str.count(sub[, start[, end]])
str.encode([encoding[, errors]])
str.endswith(suffix[, start[, end]])
str.expandtabs(tabsize=8)
str.find(sub[, start[, end]])
str.format(*args, **kwargs)
str.format_map(mapping)
str.index(sub[, start[, end]])
str.isalnum()
str.isalpha()
str.isascii()
str.isdecimal()
str.isdigit()
str.isidentifier()
str.islower()
str.isnumeric()
str.isprintable()
str.isspace()
str.istitle()
str.isupper()
str.join(iterable)
str.ljust(width[, fillchar])
str.lower()
str.lstrip([chars])
str.maketrans(x[, y[, z]])
str.partition(sep)
str.replace(old, new[, count])
str.rfind(sub[, start[, end]])
str.rindex(sub[, start[, end]])
str.rjust(width[, fillchar])
str.rsplit([sep[, maxsplit]])
str.rstrip([chars])
str.split([sep[, maxsplit]])
str.splitlines([keepends])
str.startswith(prefix[, start[, end]])
str.strip([chars])
str.swapcase()
str.title()
str.upper()
str.zfill(width)


# **For `range`:**
# Range functions
range(stop)
range(start, stop[, step])


# **For `bool`:**
# Boolean values
True
False


# **For other data types:**
# NoneType (None)
None

# Tuple methods
tuple.count(value)
tuple.index(value[, start[, stop]])

# Complex methods
complex.real
complex.imag
complex.conjugate()

# Bytes methods
bytes.decode([encoding[, errors]])
bytes.fromhex(string)

# ByteArray methods
bytearray.copy()
bytearray.count(value)
bytearray.extend(iterable)
bytearray.index(value[, start[, stop]])
bytearray.insert(i, x)
bytearray.pop([index])
bytearray.remove(value)
bytearray.reverse()

# MemoryView methods
memoryview.tolist()