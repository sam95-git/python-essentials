# Collections: Interview Preparation

## Core Questions

### 1. List versus tuple?

Both are ordered sequences. Lists are mutable and generally used for changing data; tuples are immutable and useful for fixed records or hashable composite keys.

### 2. Set versus dictionary?

A set stores unique values. A dictionary stores key-value pairs with unique keys.

### 3. What does `dict.get()` do?

It returns a key's value or a supplied default instead of raising `KeyError` when the key is absent.

### 4. What is shallow copying?

A shallow copy creates a new outer collection but keeps references to nested objects. Mutating a nested object can affect both collections.

### 5. What makes an object hashable?

It has a stable hash value and equality behavior, allowing it to be used as a dictionary key or set element. Immutable built-ins such as strings and tuples of hashable values are hashable.

### 6. What is the average complexity of dictionary lookup?

Average-case lookup, insertion, and deletion are $O(1)$, with $O(n)$ worst-case behavior in pathological collision scenarios.

## Output Questions

```python
values = [1, 2, 3]
alias = values
copy = values[:]
alias.append(4)
print(values)
print(copy)
```

**Answer:** `[1, 2, 3, 4]` and `[1, 2, 3]`.

```python
data = {"a": 1}
print(data.get("b", 0))
```

**Answer:** `0`.

```python
print({1, 1, 2} == {2, 1})
print((1, 2) < (1, 3))
```

**Answer:** `True` and `True`.

## Common Traps

- `{}` creates an empty dictionary, not an empty set; use `set()` for an empty set.
- A one-item tuple needs a trailing comma: `(1,)`.
- `remove()` raises `ValueError` when the item is absent; `discard()` does not.
- Dictionary membership checks keys, not values.
- `sort()` returns `None`; `sorted()` returns a new list.
- Mutable objects cannot be dictionary keys.

## Practice

1. Remove duplicates from a list while preserving order.
2. Count word frequencies using a dictionary.
3. Group records by a selected field.
4. Explain the difference between shallow and deep copies with nested lists.
