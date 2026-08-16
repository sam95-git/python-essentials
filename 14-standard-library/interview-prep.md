# Standard Library: Interview Preparation

## Core Questions

### 1. `random` versus `secrets`?

`random` is suitable for simulations and non-security use. `secrets` uses secure randomness for tokens, passwords, and reset links.

### 2. Why use `Counter`?

It is a dictionary subclass designed for counting hashable values and provides useful methods such as `most_common()`.

### 3. Why use `deque` for a queue?

Appending and removing from either end are efficient. Removing from the front of a list is $O(n)$ because remaining elements shift.

### 4. Why use timezone-aware datetimes?

Naive datetimes do not identify a timezone and can produce ambiguous calculations around daylight-saving transitions.

### 5. What is the purpose of `logging`?

It provides levels, handlers, formatting, and routing, making diagnostics configurable without changing application logic.

## Output Questions

```python
from collections import Counter
print(Counter("banana").most_common(1))
```

**Answer:** `[('a', 3)]`.

```python
from itertools import islice
print(list(islice(range(10), 2, 6)))
```

**Answer:** `[2, 3, 4, 5]`.

```python
from pathlib import Path
print(Path("a") / "b")
```

**Answer:** a platform-appropriate path representing `a/b`.

## Common Traps

- `random` must not generate security tokens.
- Naive and aware datetimes should not be mixed casually.
- Regular expressions can become unreadable; start with string methods.
- `subprocess.run(..., shell=True)` can create command-injection risk.
- Standard-library APIs still need input validation and error handling.

## Practice

1. Count log levels with `Counter`.
2. Build a FIFO queue with `deque`.
3. Generate a secure token with `secrets`.
4. Parse command-line options with `argparse`.
