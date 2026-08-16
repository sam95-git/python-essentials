# Operators: Interview Preparation

## Core Questions

### 1. What is the difference between `/` and `//`?

`/` performs true division and always returns a `float`. `//` performs floor division and returns the greatest integer less than or equal to the result; with float operands, its result may be a float.

### 2. What does `%` return?

It returns the remainder after floor division. Python keeps the result's sign consistent with the divisor: `-7 % 3` is `2`, while `7 % -3` is `-2`.

### 3. What is operator precedence?

It is the rule that determines which parts of an expression are evaluated first. Parentheses override the default order and should be used when they improve intent.

### 4. How does `and` or `or` short-circuit?

`and` stops at the first falsey operand; `or` stops at the first truthy operand. They return one of their operands, which makes patterns such as `value or default` possible.

### 5. What is the difference between `=` and `==`?

`=` assigns a value. `==` compares two values and returns a Boolean result. Using `=` in a condition raises `SyntaxError`.

### 6. What is the difference between `is` and `==`?

`is` compares identity; `==` compares equality. Use `is None` for the singleton `None`, and use `==` for ordinary values.

### 7. What type does `input()` return?

Always `str`. Use `int()`, `float()`, or another explicit parser before numeric operations.

### 8. Why is `eval(input())` unsafe?

`eval()` executes the supplied text as Python code. Untrusted input could run commands or access data. Explicit conversion and validation are safer.

## Output-Based Questions

### Question 1

```python
print(7 / 2)
print(7 // 2)
print(-7 // 2)
print(7 % 2)
```

**Answer:**

```text
3.5
3
-4
1
```

### Question 2

```python
print(2 ** 3 ** 2)
print(-2 ** 2)
print((-2) ** 2)
```

**Answer:**

```text
512
-4
4
```

Exponentiation is right-associative, and it has higher precedence than a unary minus on its left.

### Question 3

```python
print("" or "fallback")
print("ready" and 42)
print(0 and 10 / 0)
```

**Answer:**

```text
fallback
42
0
```

The final division is never evaluated because `0` is already falsey.

### Question 4

```python
x = 10
x += 3 * 2
print(x)
```

**Answer:** `16`.

## Common Traps

- `input()` returns text: `input() + input()` concatenates strings.
- `1 / 2` is `0.5`, while `1 // 2` is `0`.
- Floor division rounds down, not toward zero: `-3 // 2 == -2`.
- `2 ** 3 ** 2` means `2 ** (3 ** 2)`.
- `-2 ** 2` is `-4`; write `(-2) ** 2` for `4`.
- `and` and `or` return operands and short-circuit.
- Comparing floats with `==` can be unreliable because of binary representation; use a tolerance for approximate comparisons.
- Do not compare strings and numbers without an explicit conversion.

## Practice Prompts

1. Write a safe calculator that handles invalid numbers and division by zero.
2. Convert a duration in minutes to hours and remaining minutes using `divmod()`.
3. Predict the result of `10 % -3` and explain the role of floor division.
4. Build a validation expression for a score from 0 through 100 inclusive.
