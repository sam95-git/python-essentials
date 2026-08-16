# Python Decorators and Context Managers

Decorators extend or wrap callable behavior. Context managers guarantee setup and cleanup around a block.

## 1. Decorators

A decorator accepts a function and returns a replacement function. The `@decorator` syntax applies it at definition time.

```python
from functools import wraps

def announce(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		print("starting")
		return function(*args, **kwargs)
	return wrapper
```

`functools.wraps` preserves metadata such as `__name__` and the docstring. Always forward `*args` and `**kwargs` when a decorator should support arbitrary calls.

## 2. Decorator Factories

A decorator factory accepts configuration and returns a decorator:

```python
def repeat(times):
	def decorator(function):
		@wraps(function)
		def wrapper(*args, **kwargs):
			result = None
			for _ in range(times):
				result = function(*args, **kwargs)
			return result
		return wrapper
	return decorator
```

Apply decorators from the closest `@` line outward. Keep decorator behavior unsurprising and document side effects.

## 3. Context Managers

The `with` statement calls `__enter__` on entry and `__exit__` on exit. It is appropriate for files, locks, transactions, and temporary state.

```python
from contextlib import contextmanager

@contextmanager
def managed_message():
	print("enter")
	try:
		yield
	finally:
		print("exit")
```

If `__exit__` or the generator's exception-handling path returns truthy, it suppresses the exception. Suppress exceptions only deliberately.

## 4. Design Guidance

Use decorators for cross-cutting behavior such as logging, caching, authorization, and timing. Use context managers for paired resource lifecycle operations. Prefer standard tools such as `functools.lru_cache`, `contextlib`, and `asynccontextmanager` when applicable.
