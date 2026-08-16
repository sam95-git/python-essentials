# Python Data Types

Data types describe the kind of value stored in an object. Python is dynamically typed: a variable name does not have a permanent type, and the type is determined at runtime.

## 1. First Python Program

`print()` is a built-in function that sends a human-readable value to the console.

```python
print("Hello, Python!")
print("Name:", "Ada", sep=" ", end="\n")
```

Important points:

- A function call uses parentheses: `print()`.
- Arguments are separated by commas.
- `sep` separates multiple arguments; its default is a space.
- `end` is printed after the arguments; its default is a newline (`"\n"`).
- `print()` returns `None`; its main purpose is the output side effect.

An empty `print()` outputs a blank line. Common escape sequences include `\n` for newline, `\t` for tab, `\\` for a backslash, `\"` for a double quote, and `\'` for an apostrophe.

```python
print("Line one\nLine two")
print('She said "Python"')
```

## 2. Literals

A literal is a fixed value written directly in source code.

```python
42                  # integer literal
3.14                # floating-point literal
0b1010              # binary integer: 10
0o17                # octal integer: 15
0xFF                # hexadecimal integer: 255
"Python"            # string literal
True                # Boolean literal
None                # absence of a value
```

Underscores improve the readability of numeric literals: `1_000_000`. Scientific notation is supported for floats: `6.02e23`.

## 3. Core Built-in Data Types

### Numeric types

`int` represents whole numbers of arbitrary size. `float` represents decimal values using floating-point arithmetic. `complex` represents values such as `2 + 3j`.

```python
count = 10
price = 19.99
measurement = 2 + 3j
```

### Boolean type

`bool` has exactly two values: `True` and `False`. Booleans are subclasses of `int`, so `True == 1` and `False == 0`, although they should be used to express truth rather than numbers.

### Strings

`str` is an immutable sequence of Unicode characters. Use single or double quotes consistently, and use triple quotes for multi-line text.

```python
name = "Ada"
message = 'Python is readable'
quoted = "She said \"hello\"."
```

Strings support indexing, slicing, concatenation, and repetition:

```python
word = "Python"
print(word[0], word[-1])  # P n
print(word[1:4])          # yth
print("ha" * 3)           # hahaha
```

### `NoneType`

`None` represents the absence of a value. Test it with identity, not equality:

```python
result = None
if result is None:
	print("No result")
```

### Collection types

The main built-in collections are covered in the collections module, but their data types are worth recognizing:

| Type | Meaning | Mutable? | Example |
| --- | --- | --- | --- |
| `list` | Ordered collection | Yes | `[1, 2, 3]` |
| `tuple` | Ordered collection | No | `(1, 2, 3)` |
| `set` | Unique unordered values | Yes | `{1, 2, 3}` |
| `dict` | Key-value mapping | Yes | `{"language": "Python"}` |

## 4. Inspecting and Converting Types

Use `type()` to inspect an object's type. Use `isinstance()` when checking whether a value belongs to a type or its subclass.

```python
value = 10
print(type(value))
print(isinstance(value, int))
```

Common conversions:

```python
int("42")       # 42
float("3.5")    # 3.5
str(42)          # "42"
bool(0)          # False
list("cat")      # ['c', 'a', 't']
```

Conversion can fail. For example, `int("3.5")` raises `ValueError`; use `int(float("3.5"))` if truncation is intended. `bool()` follows truth-value rules: `0`, `0.0`, `""`, empty collections, and `None` are falsey; most other values are truthy.

## 5. Variables and Assignment

A variable is a name bound to an object. Assignment creates or rebinds the name; it does not copy the object automatically.

```python
first_name = "Ada"
age = 36
age = age + 1
total = 3 + 5
```

Identifier rules:

- Start with a letter or underscore.
- Continue with letters, digits, or underscores.
- Be case-sensitive: `score` and `Score` differ.
- Do not use Python keywords such as `class`, `for`, or `return`.

Prefer descriptive `snake_case` names: `total_apples`, not `ta`.

Multiple assignment is useful when values are related:

```python
apples, oranges = 3, 5
apples, oranges = oranges, apples
```

Assignment expressions and comparisons are different: `=` assigns, while `==` compares.

## 6. Quick Reference

```python
value = 25
print(type(value).__name__)
print(str(value) + " items")
```

Remember: values have types, names refer to values, and conversion creates a new value rather than changing the original object's type.
