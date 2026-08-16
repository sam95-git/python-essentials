# Python Testing and Debugging

Testing checks behavior against expectations. Debugging investigates why behavior differs. Good tests make failures small, reproducible, and informative.

## 1. Testable Code

Pure functions with explicit inputs and outputs are easy to test. Keep I/O, time, randomness, and global state at the edges of the program so core logic stays deterministic.

## 2. Assertions and `unittest`

An assertion documents an expected condition:

```python
assert 2 + 2 == 4
```

Use `unittest.TestCase` for organized automated tests:

```python
import unittest

class TestMath(unittest.TestCase):
	def test_addition(self):
		self.assertEqual(2 + 2, 4)
```

Common assertions include `assertEqual`, `assertTrue`, `assertFalse`, `assertRaises`, and `assertAlmostEqual`.

## 3. Test Boundaries and Exceptions

Test normal values, empty input, minimum and maximum values, invalid input, and expected exceptions. A passing test suite increases confidence; it does not prove the absence of all bugs.

## 4. Debugging Workflow

1. Reproduce the failure reliably.
2. Read the complete traceback from the bottom up.
3. Reduce the input to the smallest failing case.
4. Inspect assumptions and state at the failure boundary.
5. Fix the cause, not only the symptom.
6. Add a regression test and rerun the suite.

Use a debugger to set breakpoints, step through code, inspect variables, and evaluate expressions. Temporary logging or targeted print statements can help, but remove noisy diagnostics from production paths.

## 5. Test Doubles and Coverage

Mocks, stubs, and fakes isolate external systems. Mock behavior, not implementation details. Coverage shows which lines ran; it does not prove that assertions are meaningful or that all behaviors are correct.

## 6. Quality Habits

Keep tests independent and deterministic. Name tests by behavior. Run fast unit tests frequently, then broader integration tests. Use linters and type checkers as additional feedback, not replacements for tests.
