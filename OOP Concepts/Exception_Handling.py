# Feature: Exception handling allows you to gracefully handle errors and exceptions that may occur during program execution.

# Example:

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print("Result:", result)
finally:
    print("Execution completed.")