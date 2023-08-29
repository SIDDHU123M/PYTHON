## FILE HANDLING 

1. **Opening a File:** To work with a file, you first need to open it. You use the `open()` function for this. You provide the filename and the mode in which you want to open the file (read, write, append, etc.).

   ```python
   file = open("filename.txt", "r")  # Open for reading
   ```

2. **Reading from a File:** Once the file is open, you can read its content. You can read the entire content at once or read it line by line.

   ```python
   content = file.read()  # Read the entire content
   line = file.readline()  # Read one line
   ```

3. **Writing to a File:** To write data to a file, you open it in write mode ("w"). You can write strings or lines of text.

   ```python
   file = open("newfile.txt", "w")  # Open for writing
   file.write("Hello, World!\n")  # Write a line
   ```

4. **Appending to a File:** You can also append content to an existing file without overwriting its existing content. Open the file in append mode ("a").

   ```python
   file = open("existingfile.txt", "a")  # Open for appending
   file.write("This is additional content.\n")
   ```

5. **Closing a File:** After you're done with a file, it's essential to close it using the `close()` method. This frees up system resources.

   ```python
   file.close()  # Close the file
   ```

6. **Using "with" Statement:** A more recommended way to work with files is by using the `with` statement. It automatically closes the file after you're done, even if an exception is raised.

   ```python
   with open("filename.txt", "r") as file:
       content = file.read()
   ```

7. **File Iteration:** You can iterate over the lines of a file using a loop.

   ```python
   with open("filename.txt", "r") as file:
       for line in file:
           print(line)
   ```

8. **Error Handling:** Remember to handle exceptions, such as `FileNotFoundError`, that might occur when working with files.

   ```python
   try:
       file = open("nonexistent.txt", "r")
   except FileNotFoundError:
       print("File not found.")
   ```

**Note:** *Remember that file handling involves interacting with the file system, so be mindful of permissions and paths. Feel free to explore more advanced techniques and modules like `os` and `shutil` for manipulating files and directories.*

## File Modes and Permissions

STAN: Absolutely, let's delve into various file modes and permissions in Python:

- **File Modes:**
  - "r" - Read Mode: Opens the file for reading. Raises an error if the file does not exist.
  - "w" - Write Mode: Opens the file for writing. Creates a new file if it doesn't exist, and truncates (empties) the file if it does.
  - "a" - Append Mode: Opens the file for writing at the end. Creates a new file if it doesn't exist.
  - "x" - Exclusive Creation Mode: Creates a new file for writing. Raises an error if the file already exists.
  - "b" - Binary Mode: Opens the file in binary mode for reading or writing.
  - "t" - Text Mode: Opens the file in text mode (default) for reading or writing.
  
  You can combine modes, for example: "rb" for reading a binary file.

- **File Permissions:**
  - "r" - Read Permission: Allows reading from the file.
  - "w" - Write Permission: Allows writing to the file (and truncates it if it exists).
  - "x" - Execute Permission: Not applicable for files in most systems.
  
  Permissions are more relevant when dealing with directories and executable files.

Here's an example demonstrating different modes and permissions:

```python
# Read mode
with open("read_example.txt", "r") as file:
    content = file.read()
    print(content)

# Write mode
with open("write_example.txt", "w") as file:
    file.write("This is a new line.")

# Append mode
with open("append_example.txt", "a") as file:
    file.write("\nAdding more content.")

# Exclusive creation mode
try:
    with open("exclusive_example.txt", "x") as file:
        file.write("New file created.")
except FileExistsError:
    print("File already exists.")

# Binary mode
with open("binary_example.bin", "wb") as file:
    file.write(b'\x41\x42\x43')

# Text mode
with open("text_example.txt", "wt") as file:
    file.write("Text mode example.")
```