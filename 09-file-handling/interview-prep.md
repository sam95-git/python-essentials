# File Handling: Interview Preparation

## Core Questions

### 1. Why use `with open(...)`?

It creates a context manager that closes the file automatically, including when the block raises an exception.

### 2. What is the difference between `w` and `a`?

`w` truncates or creates a file. `a` preserves existing content and writes at the end.

### 3. Text mode versus binary mode?

Text mode decodes bytes into strings using an encoding. Binary mode reads and writes bytes and is appropriate for images and other non-text data.

### 4. Why specify an encoding?

The platform default can vary. Explicit encoding makes behavior reproducible across systems.

### 5. Why use `pathlib`?

It provides an object-oriented, platform-independent path API and avoids fragile manual separators.

## Output Questions

```python
from io import StringIO

stream = StringIO("a\nb\n")
print(stream.readline().strip())
print(stream.read().strip())
```

**Answer:** `a` followed by `b`.

```python
with open("missing.txt", "r") as file:
	data = file.read()
```

**Answer:** It raises `FileNotFoundError` unless the file exists.

## Common Traps

- `w` destroys existing content.
- `readlines()` can consume a large amount of memory.
- `writelines()` does not insert newlines.
- File paths are not reliably portable when hard-coded with one separator style.
- Closing a file manually in every branch is less reliable than a context manager.

## Practice

1. Count non-empty lines in a text file.
2. Copy a file using binary mode.
3. Read CSV records with `csv.DictReader`.
4. Write JSON using `json.dump` and load it back.
