Calling a function from within the same function is known as a recursive function. Recursion is a programming technique where a function calls itself in order to solve a problem. Recursive functions can be powerful and elegant, but they require careful handling to ensure that they don't lead to infinite loops.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Testing the factorial function
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")
```

Explanation of how the factorial function works:
- The base case is when `n` equals 0. In this case, the factorial is defined to be 1.
- For any other value of `n`, the function calculates the factorial by multiplying `n` with the factorial of `n - 1`. This is the recursive step.
- As the function calls itself with a decreasing value of `n`, it eventually reaches the base case, and the recursive calls start returning values.
- The returned values are then multiplied together in each step to calculate the final factorial.

For example, when `num` is 5:
- `factorial(5)` calls `factorial(4)`
- `factorial(4)` calls `factorial(3)`
- `factorial(3)` calls `factorial(2)`
- `factorial(2)` calls `factorial(1)`
- `factorial(1)` calls `factorial(0)`
- `factorial(0)` returns 1 (base case)
- `factorial(1)` returns 1 * 1 = 1
- `factorial(2)` returns 2 * 1 = 2
- `factorial(3)` returns 3 * 2 = 6
- `factorial(4)` returns 4 * 6 = 24
- `factorial(5)` returns 5 * 24 = 120

It's important to note that recursive functions must have a base case to prevent infinite recursion. Without a base case, the function would keep calling itself indefinitely, leading to a stack overflow error. Additionally, recursive functions can consume more memory and be less efficient than iterative solutions for some problems. However, for certain problems, recursion can provide a more elegant and concise solution.