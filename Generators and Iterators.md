**Generators and Iterators**

1. **Generators**
   - Functions that can be paused and resumed.
   - Use the `yield` statement to produce values.
   
2. **Yield Statement**
   - Pauses the function and returns a value to the caller.
   - Resuming the function continues execution from the `yield`.
   
3. **Iterators**
   - Objects that represent a stream of data.
   - Used to loop over a sequence of items.
   
4. **Custom Iterators**
   - Create custom iterators by implementing `__iter__` and `__next__` methods.
   - Use the `StopIteration` exception to signal the end.
   
5. **Iterable and Iterator Protocols**
   - Iterable objects implement the `__iter__` method.
   - Iterator objects implement both `__iter__` and `__next__` methods.
   
6. **Lazy Evaluation**
   - Generators allow lazy evaluation of values.
   - Values are generated one at a time as needed.

**Notes and Tips:**
- Generators provide an efficient way to generate sequences.
- Use the `yield` statement to produce values in a generator.
- Iterators allow looping over sequences without loading them entirely into memory.
- Custom iterators are created by implementing the iterator protocol methods.
- Lazy evaluation allows generating values on-the-fly.

**Instructions:**
- Use generators when generating sequences on-the-fly.
- Implement custom iterators for unique looping behavior.
- Understand the difference between iterable and iterator objects.
- Utilize generators to avoid loading large datasets into memory.
- Experiment with lazy evaluation for efficient processing.
- Consider using generators for streaming data processing.
- Explore libraries that utilize generators for efficient data manipulation.

---
**Code:**
```python
# Generators
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()
first_ten = [next(fibonacci) for _ in range(10)]

# Yield Statement
def countdown(n):
    while n > 0:
        yield n
        n -= 1

countdown_gen = countdown(5)
countdown_list = list(countdown_gen)

# Iterators
my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
first_item = next(my_iterator)
remaining_items = list(my_iterator)

# Custom Iterators
class Squares:
    def __init__(self, max_number):
        self.max_number = max_number
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.max_number:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

squares = Squares(5)
squares_list = list(squares)

# Iterable and Iterator Protocols
class EvenNumbers:
    def __init__(self, max_number):
        self.max_number = max_number
    def __iter__(self):
        self.current = 2
        return self
    def __next__(self):
        if self.current > self.max_number:
            raise StopIteration
        result = self.current
        self.current += 2
        return result

even_numbers = EvenNumbers(10)
even_list = list(even_numbers)

# Lazy Evaluation
def lazy_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

lazy_range_gen = lazy_range(5)
lazy_range_list = list(lazy_range_gen)
```

