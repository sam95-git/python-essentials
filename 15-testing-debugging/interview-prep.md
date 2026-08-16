# Testing and Debugging: Interview Preparation

## Core Questions

### 1. Unit test versus integration test?

A unit test isolates a small unit such as a function. An integration test checks interactions between components or external systems.

### 2. What makes a good test?

It is deterministic, independent, focused, readable, fast, and checks observable behavior with meaningful assertions.

### 3. What is a regression test?

A test added to ensure a previously fixed defect does not return.

### 4. What is mocking?

Replacing a dependency with a controlled test double so the test focuses on the unit under test.

### 5. Does high coverage guarantee quality?

No. Coverage measures execution, not whether assertions are correct, edge cases are covered, or the design is sound.

### 6. How do you read a traceback?

Start at the final exception type and message, then walk upward through the call stack to identify the application line and the inputs that reached it.

## Output Questions

```python
def divide(a, b):
	return a / b

try:
	divide(1, 0)
except ZeroDivisionError:
	print("handled")
```

**Answer:** `handled`.

```python
import unittest

class TestExample(unittest.TestCase):
	def test_value(self):
		self.assertEqual(2 * 3, 6)
```

**Answer:** Defining the test class does not run it; a test runner is required.

## Common Traps

- Testing only the happy path misses boundary failures.
- Mocking every dependency can make tests verify implementation rather than behavior.
- Flaky tests often depend on time, randomness, ordering, or shared state.
- Do not change production code solely to satisfy a brittle test.
- `assert` statements are not a complete validation strategy.

## Practice

1. Write tests for a leap-year function, including century boundaries.
2. Test invalid inputs with `assertRaises`.
3. Add a regression test for every bug you fix.
4. Debug a failing test by reducing it to the smallest input.
