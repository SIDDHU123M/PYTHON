**Regular Expressions**

1. **Basic Matching**
   - Use `re.search()` to find the first occurrence of a pattern.
   
2. **Character Classes**
   - Specify character sets using brackets `[ ]`.
   - Matches any character within the set.
   
3. **Quantifiers**
   - Specify how many times a character or group should occur.
   - Common quantifiers: `*`, `+`, `?`, `{n}`, `{n,}`, `{n,m}`.
   
4. **Grouping and Capturing**
   - Use parentheses to group and capture portions of a match.
   - Access captured groups using `.group(n)`.
   
5. **Alternation**
   - Use the pipe `|` to specify alternatives in a pattern.
   
6. **Anchors**
   - Use `^` and `$` to match the start and end of a line/string.
   
7. **Modifiers (Flags)**
   - Modify the behavior of the regex using flags.
   - Common flags: `re.IGNORECASE`, `re.MULTILINE`.
   
8. **Substitution**
   - Use `re.sub()` to replace matched patterns with a new string.
   
9. **Raw Strings**
   - Use raw strings (`r"pattern"`) to avoid escaping backslashes.
   
**Notes and Tips:**
- Regular expressions (regex) are powerful for pattern matching.
- Use `re.search()` to find the first occurrence of a pattern.
- Character classes allow matching any character from a set.
- Quantifiers specify the number of occurrences of a pattern.
- Grouping helps capture specific parts of a match.
- Alternation allows specifying multiple alternative patterns.
- Anchors match the start or end of a line or string.
- Flags modify regex behavior (case insensitivity, multiline, etc.).
- `re.sub()` substitutes matched patterns with new content.
- Raw strings prevent backslash escape confusion in patterns.

**Instructions:**
- Identify patterns you need to match or manipulate.
- Use `re.search()` to find and extract relevant information.
- Utilize character classes and quantifiers for flexible matching.
- Group and capture parts of a match using parentheses.
- Employ alternation for handling multiple pattern options.
- Apply anchors to ensure matches occur at specific positions.
- Modify regex behavior using appropriate flags.
- Utilize `re.sub()` for search and replace operations.
- Use raw strings to write clear and readable patterns.
---
**Code:**
```python
import re # Don't forget tp import this

# Basic Matching
pattern = r"apple"
text = "I have an apple and a banana."
match = re.search(pattern, text)
if match:
    matched_text = match.group()

# Character Classes
pattern = r"[aeiou]"
text = "Hello, World!"
vowels = re.findall(pattern, text)

# Quantifiers
pattern = r"\d{3}-\d{2}-\d{4}"
text = "My SSN is 123-45-6789."
ssn = re.search(pattern, text).group()

# Grouping and Capturing
pattern = r"(\d{3})-(\d{2})-(\d{4})"
match = re.search(pattern, text)
if match:
    full_ssn = match.group()
    area_code = match.group(1)
    group_code = match.group(2)
    serial_code = match.group(3)

# Alternation
pattern = r"cat|dog"
text = "I have a cat and a dog."
matches = re.findall(pattern, text)

# Anchors
pattern = r"^Start.*End$"
text = "Start Middle End"
match = re.search(pattern, text)

# Modifiers (Flags)
pattern = r"apple"
text = "I have an Apple and a banana."
match = re.search(pattern, text, re.IGNORECASE)

# Substitution
pattern = r"apple"
text = "I have an apple and a banana."
replaced_text = re.sub(pattern, "orange", text)

# Raw Strings
pattern = r"\d{3}"
text = "123 is a number."
matches = re.findall(pattern, text)
```