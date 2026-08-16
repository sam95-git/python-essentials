# Python Iterators and Generators

Iteration provides values one at a time. It is central to `for` loops and enables lazy, memory-efficient processing.

## 1. Iterable and Iterator

An iterable can produce an iterator through `iter()`. An iterator implements `__next__()` and raises `StopIteration` when exhausted.

```python
values = iter([1, 2, 3])
print(next(values))
print(next(values))
```

`for` handles iterator creation and `StopIteration` automatically.

## 2. Generator Functions

A function containing `yield` is a generator function. Calling it returns a generator without running the body; each `next()` resumes execution until the next `yield`.

```python
def count_up_to(limit):
	for number in range(limit):
		yield number
```

Generators are lazy and usually use less memory than building a complete list.

## 3. Generator Expressions

Generator expressions use parentheses and are useful for streaming transformations:

```python
total = sum(number * number for number in range(1_000_000))
```

Unlike a list comprehension, the expression does not materialize all values at once.

## 4. `yield from` and Pipelines

`yield from iterable` delegates iteration to another iterable or generator:

```python
def flatten(groups):
	for group in groups:
		yield from group
```

Generators compose naturally into pipelines where each stage transforms or filters a stream.

## 5. Generator State and Limits

Generator state persists between yields. A generator can be consumed only once unless a new generator is created. Avoid retaining unnecessary references that prevent streamed data from being released.

Use ordinary functions when a result is small and repeated traversal is needed; use generators for large or one-pass data.
