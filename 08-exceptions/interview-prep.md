# Exceptions: Interview Preparation

## Core Questions

### 1. What is the difference between `SyntaxError` and an exception?

`SyntaxError` occurs when Python cannot parse the source. Other exceptions usually arise while syntactically valid code is executing.

### 2. How does `try-except-else-finally` work?

`try` contains risky code, `except` handles matching failures, `else` runs only after success, and `finally` runs regardless of success or failure.

### 3. Why catch specific exceptions?

Specific handling avoids hiding unrelated bugs and lets the program respond appropriately to different failures.

### 4. What is the difference between `raise` and `return`?

`return` sends a normal result to the caller. `raise` interrupts normal flow and reports an exceptional condition.

### 5. What is exception chaining?

`raise ApplicationError("...") from original_error` preserves the original cause while exposing a domain-level exception.

## Output Questions

```python
try:
	print(10 / 0)
except ZeroDivisionError:
	print("zero")
else:
	print("success")
finally:
	print("done")
```

**Answer:** `zero` followed by `done`.

```python
try:
	int("abc")
except (TypeError, ValueError):
	print("invalid")
```

**Answer:** `invalid`.

```python
def value():
	try:
		return 1
	finally:
		return 2

print(value())
```

**Answer:** `2`. A return in `finally` overrides the earlier return; avoid this confusing pattern.

## Common Traps

- A bare `except` also catches programming errors and interrupts; prefer specific exceptions.
- `finally` normally runs even when `return` is used.
- Do not catch `Exception` merely to make an error disappear.
- An exception variable may be cleared after the `except` block; preserve what you need explicitly.
- `assert` is for developer invariants, not user-input validation, because optimizations can remove assertions.

## Practice

1. Build a safe integer parser with a clear error message.
2. Create a custom exception for an invalid account state.
3. Translate a `KeyError` into a domain-specific configuration error.
4. Test all expected exception and success paths.
