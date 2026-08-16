# Python Standard Library

The standard library provides batteries-included tools without third-party installation. Learn to recognize the right module before writing a custom implementation.

## 1. Common Modules

| Module | Useful tools |
| --- | --- |
| `math` | Numeric functions and constants |
| `statistics` | Mean, median, mode, spread |
| `pathlib` | Platform-independent paths |
| `datetime` | Dates, times, and durations |
| `collections` | `Counter`, `defaultdict`, `deque` |
| `itertools` | Efficient iterator building blocks |
| `functools` | `reduce`, caching, partial calls |
| `re` | Regular expressions |
| `json` | JSON serialization |
| `csv` | CSV reading and writing |
| `os` and `sys` | Operating-system and interpreter interfaces |
| `logging` | Configurable application logs |

## 2. Collections Helpers

```python
from collections import Counter, defaultdict, deque

counts = Counter("banana")
groups = defaultdict(list)
queue = deque([1, 2])
queue.append(3)
queue.popleft()
```

## 3. Dates and Randomness

Use timezone-aware datetimes for real-world timestamps. Use `secrets` for security-sensitive tokens; `random` is not cryptographically secure.

```python
from datetime import date, timedelta

tomorrow = date.today() + timedelta(days=1)
```

## 4. Regular Expressions and Serialization

Use `re` for pattern matching when simpler string methods are insufficient. Use `json` for interoperable structured text and validate untrusted data after parsing.

## 5. Logging and Command-Line Tools

Use `logging` rather than scattered `print()` calls in applications. Use `argparse` for command-line interfaces. Use `subprocess` carefully and never pass untrusted shell text to `shell=True`.

## 6. Choosing Dependencies

Prefer the standard library for small, stable needs. Add third-party dependencies when they provide meaningful capability, maintainability, or performance. Pin and document dependencies for reproducible environments.
