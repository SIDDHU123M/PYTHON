**File Handling in Python:**


1. **Opening a File:**

   - To open a file, you use the built-in `open()` function. It takes two arguments: the file path and the mode in which you want to open the file (`'r'` for reading, `'w'` for writing, `'a'` for appending, and more).


   ```python

   file_path = 'example.txt'

   file = open(file_path, 'r')  # Open for reading

   ```

2. **Reading from a File:**

   - Once a file is open for reading, you can use various methods to read its contents.

   - `read()`: Reads the entire content of the file as a single string.

   - `readline()`: Reads a single line from the file.

   - `readlines()`: Reads all lines of the file and returns them as a list.


   ```python

   content = file.read()  # Read entire content as a string

   line = file.readline()  # Read a single line

   lines = file.readlines()  # Read all lines into a list

   ```


3. **Writing to a File:**

   - To open a file for writing, use `'w'` mode. This mode creates a new file if it doesn't exist or overwrites the existing content if it does.


   ```python

   file_path = 'output.txt'

   with open(file_path, 'w') as file:

       file.write("Hello, world!\n")

       file.write("This is a new line.")

   ```


4. **Appending to a File:**

   - Use `'a'` mode to open a file for appending. This mode adds content to the end of the file without overwriting existing content.


   ```python

   with open(file_path, 'a') as file:

       file.write("\nAppending a new line.")

   ```


5. **Closing a File:**

   - It's important to close files after you're done with them to free up system resources.

   - You can use the `close()` method or use a `with` statement, which automatically closes the file when you're done.

   ```python

   file.close()  # Explicitly close the file

   ```


**Using `with` Statements:**

- The `with` statement is a recommended way to work with files. It ensures that the file is properly closed after use, even if an exception is raised.


**Reading and Writing Example:**

```python

# Reading from a file

with open('sample.txt', 'r') as file:

    content = file.read()

    print(content)


# Writing to a file

with open('output.txt', 'w') as file:

    file.write("This is a line.\n")

    file.write("Another line.")

```


**Output:**

```

This is the content of the sample file.

```


**Note:** Remember, proper error handling is important when working with files to handle cases where files might not exist or operations fail due to various reasons. Always close files after you're done to avoid potential issues and resource leaks.