# Python Exceptions, Testing, and Debugging

Exceptions report errors that occur while valid Python code is running. Handling expected exceptions lets a program recover, explain a problem, or clean up resources instead of terminating with an unhelpful message.

## Errors and Exceptions

- A **syntax error** means the source does not follow Python grammar; fix the code rather than trying to handle it at runtime.
- An **exception** happens during execution, such as converting invalid input or dividing by zero.
- A **bug** is an unintended behavior caused by a defect in the program. Debugging is the process of finding and correcting its cause.
- Bad input and faulty code are different problems: validate expected input formats and handle expected runtime failures, but do not silently hide programming defects.

The final line of a traceback names the exception and usually describes its cause. The preceding traceback lines show the calls that led to it.

## Common Built-in Exceptions

| Exception | Typical cause |
| --- | --- |
| `ValueError` | Correct type, unacceptable value, e.g. `int("hello")` |
| `TypeError` | Operation or function receives an unsupported type, e.g. `10 / "2"` |
| `ZeroDivisionError` | `/`, `//`, or `%` with a zero divisor |
| `IndexError` | Sequence index is out of range |
| `KeyError` | Dictionary key is absent |
| `NameError` | Name is not defined in the current scope |
| `AttributeError` | Requested attribute or method does not exist |
| `FileNotFoundError` | A requested file does not exist |
| `SyntaxError` | Python grammar is invalid; fix the source code |
| `KeyboardInterrupt` | User interrupts execution, commonly with Ctrl+C |

## Handling Exceptions with `try` and `except`

Put the operation that may fail inside `try`; handle the specific expected exception in `except`. If an exception occurs, the remaining statements in that `try` block are skipped and a matching handler runs.

```python
try:
	number = int("42")
except ValueError:
	print("Please provide an integer.")
else:
	print("Parsed:", number)
finally:
	print("Parsing attempt finished.")
```

- `except` handles a matching exception.
- `else` runs only if the `try` block completes without an exception.
- `finally` runs whether the operation succeeds or fails; use it for cleanup that must happen in either case.
- When using multiple handlers, put specific exceptions before more general ones.
- Avoid bare `except:`: it can catch unexpected programming errors and interrupts. Catch the narrowest expected exception.

## Multiple Exceptions and Exception Details

Use separate handlers when errors require different responses. Several exception types can share one handler when the recovery behavior is the same.

```python
try:
	value = int(user_text)
	reciprocal = 1 / value
except ValueError:
	print("Enter a whole number.")
except ZeroDivisionError:
	print("Zero has no reciprocal.")
else:
	print("Reciprocal:", reciprocal)
```

You can capture an exception object to report its detail or preserve its cause:

```python
try:
	value = int("not a number")
except ValueError as error:
	print("Conversion failed:", error)
```

## Raising Exceptions

Raise an exception when a function receives invalid data or cannot fulfill its contract. Use standard exception types where appropriate and provide a useful message.

```python
def reciprocal(value):
	if value == 0:
		raise ValueError("value must not be zero")
	return 1 / value
```

Custom exceptions can represent domain-specific errors:

```python
class ConfigurationError(Exception):
	"""Raised when application configuration is invalid."""


def load_configuration():
	raise ConfigurationError("Missing database host")


try:
	load_configuration()
except ConfigurationError as error:
	print(error)
```

Use exception chaining (`raise NewError(...) from error`) when translating one meaningful error into another, while keeping its original cause.

## Solved Example: Read and Calculate a Reciprocal

The conversion can raise `ValueError`; division can raise `ZeroDivisionError`. Handle them separately so the user receives the right explanation.

```python
def reciprocal_from_text(text):
	try:
		value = int(text)
	except ValueError:
		return "Please enter an integer."

	if value == 0:
		return "Zero has no reciprocal."
	return 1 / value


print(reciprocal_from_text("4"))
print(reciprocal_from_text("0"))
print(reciprocal_from_text("hello"))
```

Expected results: `0.25`, `Zero has no reciprocal.`, and `Please enter an integer.`

The function catches only the expected conversion failure. It checks zero explicitly and returns a meaningful result; a larger application could instead raise a documented exception.

## Testing Execution Paths

Testing cannot prove that software has no bugs. It can reveal defects and increase confidence when tests cover expected behavior, boundary cases, and error paths.

- Identify each decision branch and test inputs that exercise every path.
- For the reciprocal example, test a positive integer, a negative integer, zero, and invalid text.
- Include boundary values such as empty input, minimum/maximum values, and one step outside a valid range.
- Add a regression test whenever a defect is fixed.
- Ask another person to review the code when possible; authors can overlook assumptions in their own work.

### Unit tests with `unittest`

Unit tests check a small function or component in isolation. Keep core logic deterministic so it is easy to test.

```python
import unittest


def reciprocal(value):
	if value == 0:
		raise ValueError("value must not be zero")
	return 1 / value


class TestReciprocal(unittest.TestCase):
	def test_positive_value(self):
		self.assertEqual(reciprocal(4), 0.25)

	def test_negative_value(self):
		self.assertEqual(reciprocal(-2), -0.5)

	def test_zero_raises(self):
		with self.assertRaises(ValueError):
			reciprocal(0)


if __name__ == "__main__":
	unittest.main()
```

Common assertions include `assertEqual`, `assertTrue`, `assertFalse`, `assertRaises`, and `assertAlmostEqual` for approximate floating-point results.

## Debugging Workflow

1. Reproduce the failure with a small, repeatable input.
2. Read the full traceback, starting with the exception type and message at the bottom.
3. Trace the relevant variables and calls back to the point where the state became incorrect.
4. Reduce the problem to the smallest failing example.
5. Fix the underlying cause, not just the visible symptom.
6. Add a regression test and rerun the relevant test suite.

### Debugging tools and habits

- A **debugger** lets you set breakpoints, step through code, inspect variables, and examine the call stack.
- **Print/log debugging** can expose control flow and values; remove temporary output once the defect is fixed. Prefer the `logging` module for application diagnostics.
- **Rubber-duck debugging** means explaining the code and its assumptions step by step; the act of explanation often reveals the mistake.
- Isolate suspicious code, substitute known values for user input, review recent changes, and take a break if stuck.
- Check every meaningful execution path; interpreted code may not execute a faulty line if tests never enter that branch.

## Good Exception and Testing Practices

- Catch only exceptions you can handle meaningfully.
- Keep `try` blocks small so it is clear which operation may fail.
- Do not use exceptions to disguise bugs or continue with corrupt state.
- Do not use `assert` to validate untrusted user input; assertions may be disabled and are intended for developer invariants.
- Keep tests independent, deterministic, and focused on observable behavior.
- Coverage shows which code ran; it does not prove assertions are useful or behavior is correct.

## Final Quiz: Interview Practice

### Question 1

What is printed if the user enters `0`?

```python
try:
	value = int(input("Enter a value: "))
	print(value / value)
except ValueError:
	print("Bad input...")
except ZeroDivisionError:
	print("Very bad input...")
except:
	print("Booo!")
```

**Answer:** `Very bad input...`; converting `0` succeeds, then `value / value` raises `ZeroDivisionError`.

### Question 2

What happens if the user enters `0`?

```python
value = input("Enter a value: ")
print(10 / value)
```

**Answer:** `input()` returns the string `"0"`. Dividing an integer by a string raises an unhandled `TypeError`; convert the input to a number before arithmetic.
