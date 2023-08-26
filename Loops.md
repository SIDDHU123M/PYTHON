Python supports two main types of loops: `for` loops and `while` loops. I'll provide explanations, examples, outputs, characteristics, and definitions for both types of loops.

**`for` Loops:**

1. **Definition:** A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence.


2. **Example:**

   ```python
   fruits = ["apple", "banana", "cherry"]

   for fruit in fruits:

       print(fruit)
   ```


3. **Output:**

   ```
   apple

   banana

   cherry
   ```


4. **Characteristics:**

   - `for` loops are used when you know the number of iterations in advance.

   - They automatically iterate through each element in the sequence.


**`while` Loops:**


1. **Definition:** A `while` loop repeatedly executes a block of code as long as a specified condition is `True`.


2. **Example:**

   ```python
   count = 0

   while count < 5:

       print(count)

       count += 1
   ```


3. **Output:**

   ```
   0
   1
   2
   3
   4
   ```


4. **Characteristics:**

   - `while` loops are used when you don't know the number of iterations in advance.

   - They continue executing as long as the given condition remains `True`.

   - Be careful to ensure the loop condition eventually becomes `False` to prevent infinite loops.


**Loop Control Statements:**


1. **`break`:** Terminates the loop prematurely, even if the loop condition is still satisfied.

   ```python
   for num in range(5):

       if num == 3:

           break

       print(num)
   ```


2. **`continue`:** Skips the current iteration and moves to the next iteration of the loop.

   ```python
   for num in range(5):

       if num == 3:

           continue

       print(num)
   ```


**Nested Loops:**

You can have loops within loops (nested loops) to perform more complex operations. Just be cautious about the complexity and performance implications.


**Loop Definitions:**

1. **`for` Loop Definition:** A `for` loop is a control structure that iterates over a sequence of items and executes a block of code for each item in the sequence.


2. **`while` Loop Definition:** A `while` loop is a control structure that repeatedly executes a block of code as long as a specified condition is satisfied.


**Loop Example with Nested `for` and `while` Loops:**

```python
for i in range(3):

    print(f"Outer loop iteration {i}")

    j = 0

    while j < 2:

        print(f"  Inner loop iteration {j}")

        j += 1
```

**Output:**

```
Outer loop iteration 0

  Inner loop iteration 0

  Inner loop iteration 1

Outer loop iteration 1

  Inner loop iteration 0

  Inner loop iteration 1

Outer loop iteration 2

  Inner loop iteration 0

  Inner loop iteration 1
```

In summary, loops are powerful tools for automating repetitive tasks in programming. Use `for` loops when you know the number of iterations, and `while` loops when you don't. Be cautious with loop control statements and nested loops to ensure your code is efficient and produces the desired results.