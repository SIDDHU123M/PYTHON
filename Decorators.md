**Decorators**

1. **Simple Decorator**
   - A function that takes another function as an argument.
   - Modifies or extends the behavior of the passed function.
   - Use the `@decorator_name` syntax to apply decorators.
   
2. **Decorator with Arguments**
   - Decorators can accept additional arguments.
   - A decorator function returns a new function that wraps the original function.
   
3. **Decorator Classes**
   - Decorators can also be implemented as classes.
   - Use the `__call__` method to define the decorator's behavior.

**Notes and Tips:**
- Decorators allow modifying or extending the behavior of functions.
- They are applied using the `@decorator_name` syntax above the function.
- Decorators can be simple functions or classes.
- Decorator functions can accept arguments for customization.
- Decorator classes require the `__call__` method for execution.

**Instructions:**
- Identify functions that can benefit from common modifications.
- Implement decorators to add behavior without modifying original functions.
- Utilize decorator arguments to customize decorator behavior.
- Experiment with both function-based and class-based decorators.
- Use decorators to measure execution time, log actions, and more.
- Be cautious when using decorators on performance-sensitive code.

```python
# Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# Decorator Classes
class TimingDecorator:
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        import time
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result

@TimingDecorator
def slow_function():
    import time
    time.sleep(2)
    print("Function executed!")

slow_function()
```