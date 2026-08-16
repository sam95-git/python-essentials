# Iterators and Generators: Interview Preparation

## Core Questions

### 1. Iterable versus iterator?

An iterable can produce an iterator. An iterator stores iteration state and supplies the next value through `__next__()`.

### 2. What does `yield` do?

It returns a value and suspends the generator, preserving local state for the next request.

### 3. Generator versus list?

A generator is lazy and one-pass; a list is eager, stores all values, and can be indexed and reused.

### 4. What is `StopIteration`?

It signals that an iterator has no more values. A `for` loop catches it internally.

### 5. What does `yield from` do?

It delegates iteration to another iterable or generator and forwards its values.

## Output Questions

```python
def numbers():
	print("start")
	yield 1
	print("middle")
	yield 2

items = numbers()
print("created")
print(next(items))
print(next(items))
```

**Answer:** `created`, `start`, `1`, `middle`, `2`. The body begins on the first `next()`.

```python
generator = (number * 2 for number in range(3))
print(list(generator))
print(list(generator))
```

**Answer:** `[0, 2, 4]` followed by `[]`; the generator was consumed.

## Common Traps

- Calling a generator function does not execute its body immediately.
- Iterators are often exhausted after one pass.
- `next(iterator, default)` avoids `StopIteration` by returning a default.
- A generator improves memory use, not necessarily CPU time.
- Do not use a generator when random access or repeated traversal is required.

## Practice

1. Write a generator that yields prime numbers.
2. Build a lazy pipeline that strips and filters input lines.
3. Flatten nested iterables with `yield from`.
4. Compare memory behavior of a list comprehension and generator expression.
