## Special Characters

- **Newline (\n):** Represents a newline character. It's used to start a new line in the text.
- **Tab (\t):** Represents a tab character. It's used for indentation or aligning content.
- **Backslash (\\):** Represents the literal backslash character itself.
- **Single Quote (\'):** Represents the literal single quote character within a single-quoted string.
- **Double Quote (\"):** Represents the literal double quote character within a double-quoted string.
- **Carriage Return (\r):** Represents a carriage return character, which moves the cursor to the beginning of the line.
- **Unicode Escape (\u and \U):** Represents Unicode characters using their Unicode code points. For example, "\u20AC" represents the Euro sign (€).
- **Hexadecimal Escape (\x):** Represents characters using their hexadecimal ASCII codes. For example, "\x41" represents the character 'A'.

Here's an example showcasing some of these escape sequences:

```python
print("Line 1\nLine 2")
print("This is a tab:\tTabbed text")
print("This is a backslash: \\")
print('This is a single quote: \'')
print("This is a double quote: \"")

# Unicode and Hexadecimal escapes
print("\u20AC")  # Euro sign (€)
print("\x41")    # 'A'
```