# Decorators and Context Managers: Interview Preparation

## Core Questions

### 1. What is a decorator?

A callable that receives a function or class and returns a modified or wrapped callable.

### 2. Why use `functools.wraps`?

It copies metadata from the wrapped function, preserving names, documentation, and useful introspection behavior.

### 3. What is a decorator factory?

A function that receives configuration and returns a decorator. It adds one extra nesting level.

### 4. What methods define a context manager?

`__enter__` runs on entry and `__exit__` runs on exit. `contextlib.contextmanager` provides a generator-based alternative.

### 5. How can a context manager suppress an exception?

`__exit__` can return truthy, or a generator context manager can handle the exception without re-raising it. This should be rare and explicit.

## Output Questions

```python
def decorator(function):
	def wrapper():
		return "wrapped " + function()
	return wrapper

@decorator
def value():
	return "value"

print(value())
```

**Answer:** `wrapped value`.

```python
from contextlib import contextmanager

@contextmanager
def demo():
	print("in")
	yield
	print("out")

with demo():
	print("body")
```

**Answer:** `in`, `body`, `out`.

## Common Traps

- A decorator runs when the decorated definition is evaluated, while its wrapper runs when called.
- Forgetting to return the wrapper can replace a function with `None`.
- Decorators can change signatures, metadata, exceptions, and side effects.
- Cleanup belongs in `finally` or `__exit__`.
- Do not suppress exceptions accidentally.

## Practice

1. Write a timing decorator using `time.perf_counter()`.
2. Build a retry decorator for a selected exception.
3. Create a context manager that temporarily changes a working directory.
4. Preserve decorated function metadata with `wraps`.
