# Python File Handling

File handling connects a program to persistent data. Use context managers, explicit encodings, and predictable paths.

## 1. Opening Files

```python
with open("notes.txt", "r", encoding="utf-8") as file:
	content = file.read()
```

The `with` statement closes the file even when an exception occurs. Common modes are `r` (read), `w` (write and truncate), `a` (append), and `x` (create exclusively). Add `b` for binary mode.

## 2. Reading and Writing

Useful methods include `read`, `readline`, `readlines`, and iteration over the file object. For large files, iterate line by line instead of loading everything into memory.

```python
with open("input.txt", encoding="utf-8") as source:
	for line in source:
		print(line.rstrip())

with open("output.txt", "w", encoding="utf-8") as target:
	target.write("Python\n")
```

`write()` expects a string and returns the number of written characters. Use `writelines()` for an iterable of strings; it does not add separators automatically.

## 3. Paths

Prefer `pathlib.Path` over manual string concatenation:

```python
from pathlib import Path

path = Path("data") / "records.txt"
if path.exists():
	text = path.read_text(encoding="utf-8")
```

`Path` supports `exists`, `is_file`, `mkdir`, `glob`, `read_text`, and `write_text`.

## 4. Structured Data

Use standard parsers for structured formats rather than splitting text manually:

```python
import json

payload = {"language": "Python", "version": 3}
text = json.dumps(payload, indent=2)
restored = json.loads(text)
```

CSV data should use the `csv` module, which handles quoting and delimiters correctly.

## 5. Safety and Reliability

- Use `encoding="utf-8"` for text unless another encoding is required.
- Do not build paths from untrusted input without validation.
- Catch expected `OSError` subclasses and report actionable context.
- Use temporary directories in tests.
- For critical writes, write to a temporary file and replace the destination after success.
