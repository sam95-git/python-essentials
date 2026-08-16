# Python Exceptions

Exceptions report abnormal situations during execution. Handling them lets a program recover from expected failures without hiding programming defects.

## 1. Common Error Categories

- `SyntaxError`: code violates Python grammar.
- `NameError`: a name is not defined.
- `TypeError`: an operation receives an inappropriate type.
- `ValueError`: the type is valid but the value is unacceptable.
- `IndexError`: a sequence index is out of range.
- `KeyError`: a dictionary key is absent.
- `AttributeError`: an object lacks an attribute or method.
- `ZeroDivisionError`: division or modulo uses zero.

Syntax errors must be fixed in the source. Runtime exceptions can sometimes be handled when the situation is expected and recoverable.

## 2. `try` and `except`

Put only the risky operation in the `try` block and handle specific exceptions:

```python
try:
	number = int(text)
except ValueError:
	number = 0
```

Multiple `except` blocks are checked top to bottom. Put specific exceptions before broad ones. Avoid a bare `except` unless you immediately re-raise or have a strong reason to catch everything.

## 3. `else` and `finally`

`else` runs only when the `try` block succeeds. `finally` runs whether an exception occurred or not and is useful for cleanup.

```python
try:
	result = 10 / divisor
except ZeroDivisionError:
	result = None
else:
	print("calculation succeeded")
finally:
	print("calculation finished")
```

## 4. Raising Exceptions

Use `raise` when a function receives invalid input or detects a violated contract:

```python
def percentage(value):
	if not 0 <= value <= 100:
		raise ValueError("value must be between 0 and 100")
	return value
```

Custom exceptions can represent domain-specific failures:

```python
class ConfigurationError(Exception):
	pass
```

Use exception chaining with `raise NewError(...) from error` when translating a lower-level error.

## 5. Good Exception Practices

- Catch the narrowest expected exception.
- Do not use exceptions to conceal bugs or silently continue with corrupt state.
- Keep `try` blocks small.
- Add useful context to error messages.
- Preserve the original exception when re-raising or translating.
- Use `with` for resources that need reliable cleanup.
