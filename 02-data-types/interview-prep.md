# Data Types: Interview Preparation

## Core Questions

### 1. Is Python statically or dynamically typed?

Python is dynamically typed. Names do not require a declared type and may be rebound to objects of different types. Python is also strongly typed: it does not silently combine unrelated types in operations such as `"2" + 2`.

### 2. What is the difference between `type()` and `isinstance()`?

`type(value)` returns the exact type. `isinstance(value, SomeType)` checks whether the value is an instance of that type or a subclass, so it is generally more flexible for validation.

### 3. What is the difference between mutable and immutable types?

Mutable objects can be changed in place, such as `list`, `dict`, and `set`. Immutable objects cannot be changed after creation, such as `int`, `float`, `bool`, `str`, and `tuple`. An operation on an immutable value creates a new object.

### 4. What does `None` mean?

`None` is the singleton value representing no value or no result. Use `value is None` and `value is not None` to test it.

### 5. What is the difference between `==` and `is`?

`==` compares values. `is` compares object identity. Use `is` for singleton checks such as `None`, not for ordinary value comparison.

### 6. What does `bool()` do?

It converts a value using its truth value. `0`, `0.0`, `""`, empty collections, and `None` are falsey. Non-empty collections and most other objects are truthy.

### 7. What happens when converting invalid input?

`int("abc")` and `float("abc")` raise `ValueError`. `int(None)` raises `TypeError`. Handle expected conversion failures with `try`/`except`.

### 8. Why does `int("3.5")` fail?

The string is not written as an integer literal. Convert through a float when truncation is explicitly desired: `int(float("3.5"))` gives `3`.

## Output-Based Questions

### Question 1

```python
value = "10"
print(type(value).__name__)
print(value * 2)
```

**Answer:**

```text
str
1010
```

### Question 2

```python
print(bool("False"))
print(bool(0))
print(True == 1)
```

**Answer:**

```text
True
False
True
```

The string is non-empty, so its contents do not matter to `bool()`.

### Question 3

```python
items = [1, 2]
alias = items
alias.append(3)
print(items)
```

**Answer:** `[1, 2, 3]`. Both names refer to the same mutable list.

### Question 4

```python
result = None
print(result is None)
print(result == 0)
```

**Answer:**

```text
True
False
```

## Common Traps

- `input()` always returns `str`, even when the user enters digits.
- `"10" + "5"` is `"105"`; it is not numeric addition.
- `"10" * 2` is `"1010"`; string repetition is valid.
- `4` and `4.0` compare equal, but their types are different.
- `type(True)` is `bool`, although `bool` is a subclass of `int`.
- `list.copy()` is shallow; nested objects are still shared.
- Never use `is` as a replacement for `==` when comparing ordinary values.

## Practice Prompts

1. Write a function that accepts a value and returns its type name.
2. Safely convert a user-entered value to `float`, returning `None` for invalid input.
3. Explain why `a = b = []` can cause unexpected shared mutations.
4. Predict the output of `print(bool([]), bool([False]))` and explain why.
