# Strings: Interview Preparation

## Core Questions

### 1. Are Python strings mutable?

No. String operations return new string objects. Individual characters cannot be assigned.

### 2. Why use `join()` instead of repeated concatenation?

`join()` expresses the operation clearly and avoids repeatedly creating intermediate strings, especially inside loops.

### 3. What is the difference between `find()` and `index()`?

Both search for a substring. `find()` returns `-1` when absent; `index()` raises `ValueError`.

### 4. `lower()` versus `casefold()`?

Both support case normalization. `casefold()` is more aggressive and is preferred for Unicode-aware case-insensitive comparisons.

### 5. What is the difference between `split()` and `partition()`?

`split()` can produce many pieces and returns a list. `partition()` splits at the first separator and always returns a three-item tuple.

## Output Questions

```python
text = "Python"
text.lower()
print(text)
```

**Answer:** `Python`; the original string was not changed.

```python
print("a,b,c".split(","))
print("a,b,c".partition(","))
```

**Answer:** `['a', 'b', 'c']` and `('a', ',', 'b,c')`.

```python
parts = ["learn", "Python"]
print(" ".join(parts))
```

**Answer:** `learn Python`.

## Common Traps

- `input()` returns a string, even for numeric text.
- `strip()` removes characters from the ends, not an arbitrary substring.
- `split()` with no argument treats consecutive whitespace as one separator.
- `is` checks identity; use `==` for string values.
- `"10" < "2"` compares lexicographically, not numerically.
- `replace()` returns a new string and does not mutate the original.

## Practice

1. Normalize a sentence and count its words.
2. Check whether a string is a palindrome after removing spaces and case differences.
3. Convert `key=value` text into a dictionary entry.
4. Format a report using f-strings with numeric precision.
