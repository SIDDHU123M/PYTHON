
**Exception Handling**

1. **try-except Block**
   - Used to catch and handle exceptions gracefully.
   - Syntax: `try: ... except ExceptionType: ...`
   - The `except` block executes if an exception of the specified type occurs.
   - Use `else` block for code that runs when no exception occurs.
   
2. **Custom Exceptions**
   - Define your own exception classes by inheriting from `Exception`.
   - Raise custom exceptions using the `raise` statement.
   
3. **Handling Multiple Exceptions**
   - Use multiple `except` blocks to handle different exceptions.
   - Ensure proper order of exception handling.
   
4. **finally Block**
   - Code within the `finally` block executes regardless of exceptions.
   - Used for cleanup or resource management.
   
5. **Error Return**
   - Return error messages when exceptions occur.
   - Improve user experience by providing informative messages.
   
6. **Assertions**
   - Check for expected conditions using assertions.
   - Raise an error if the condition is not met.

**Notes and Tips:**
- Exception handling prevents program crashes due to errors.
- Handle specific exceptions to provide tailored error messages.
- Custom exceptions add clarity to error handling in complex code.
- The `else` block is executed when no exception occurs in the `try` block.
- The `finally` block is used for cleanup, closing files, etc.
- Use assertions to ensure expected conditions are met.
- Error returns provide informative feedback to users.
- Avoid using bare `except` to catch all exceptions; be specific.

**Instructions:**
- Identify parts of your code that could raise exceptions.
- Use `try-except` blocks to handle expected errors.
- Customize exception handling messages for better user experience.
- Employ custom exceptions for complex error handling.
- Ensure proper use of `finally` for cleanup operations.
- Utilize assertions to check conditions that should always be true.
- Implement error returns to handle exceptions gracefully.
- Remember to use assertions only for debugging purposes.


```python
# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 'Error: Division by zero'
else:
    result = 'No error occurred'

# Custom Exceptions
class MyCustomError(Exception):
    pass

try:
    if condition:
        raise MyCustomError("This is a custom error.")
except MyCustomError as error:
    error_message = str(error)

# Handling Multiple Exceptions
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    result = 'Invalid input: Not a number'
except ZeroDivisionError:
    result = 'Error: Division by zero'
else:
    result = 'Calculation successful'

# Finally Block
try:
    # Code that might raise an exception
except MyException:
    # Handle the exception
finally:
    # Code that runs regardless of an exception

# Error Return
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return 'Error: Division by zero'
    else:
        return result

# Assertions
def calculate_square_root(x):
    assert x >= 0, "Input must be non-negative"
    return x ** 0.5
```
