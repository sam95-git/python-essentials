# Python Strings

Strings are immutable sequences of Unicode characters. They support indexing, slicing, iteration, formatting, and many useful methods.

## 1. Creating and Indexing Strings

```python
single = 'Python'
double = "Python"
multiline = """line one
line two"""

word = "Python"
print(word[0], word[-1], word[1:4])
```

Indexing returns one-character strings. Slicing uses an exclusive stop: `text[start:stop:step]`. Strings cannot be changed in place.

## 2. Escape Sequences and Raw Strings

Common escapes include `\n`, `\t`, `\\`, `\"`, and `\'`.

```python
print("Line one\nLine two")
path = r"C:\\Users\\Ada"
```

Raw strings are useful for paths and regular-expression patterns, but a raw string cannot end with a single backslash.

## 3. Concatenation and Formatting

Use `+` for concatenation and `*` for repetition, but prefer f-strings for interpolation:

```python
name = "Ada"
score = 95
print(f"{name} scored {score}%")
print(f"{score / 10:.1f}")
```

`str.format()` and percent formatting exist for legacy code. Avoid repeated `+` concatenation in loops; collect pieces and use `"".join(pieces)`.

## 4. Useful Methods

- Case: `upper`, `lower`, `casefold`, `title`, `capitalize`
- Whitespace: `strip`, `lstrip`, `rstrip`
- Search: `find`, `index`, `count`, `startswith`, `endswith`
- Replacement: `replace`, `translate`
- Splitting: `split`, `rsplit`, `splitlines`, `partition`
- Joining: `separator.join(iterable)`

Methods return new strings because strings are immutable.

```python
text = "  Python, code  "
clean = text.strip().replace(",", "")
words = clean.split()
print("-".join(words))
```

## 5. Validation and Unicode

Methods such as `isdigit()`, `isalpha()`, `isalnum()`, and `isspace()` test character properties. They do not validate every possible numeric format.

Use `casefold()` for robust case-insensitive comparisons. Python strings are Unicode, so length and indexing count code points, not necessarily user-perceived grapheme clusters.

## 6. Immutability and Performance

Operations like `text += piece` create a new string. For many pieces, use a list and `join()`:

```python
parts = ["Python", "is", "readable"]
sentence = " ".join(parts)
```

Keep external text encoding explicit when reading or writing files, commonly `encoding="utf-8"`.
