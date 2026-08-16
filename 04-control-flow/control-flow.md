# Python Control Flow

Control flow determines which statements run, how often they run, and when a loop stops. Python uses Boolean conditions and indentation to represent execution paths.

## 1. Conditions and Comparisons

Comparison operators return `True` or `False`:

| Operator | Meaning |
| --- | --- |
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `>=` | Greater than or equal to |
| `<` | Less than |
| `<=` | Less than or equal to |

Do not confuse assignment with comparison:

```python
score = 80       # assignment
is_passing = score >= 50  # comparison
```

Comparisons can be chained:

```python
if 0 <= score <= 100:
	print("Valid score")
```

## 2. The `if` Statement

An `if` block runs only when its condition is truthy. A colon starts the block, and indentation defines its body.

```python
temperature = 25
if temperature > 20:
	print("Warm day")
```

Use `else` for the alternative path:

```python
if age >= 18:
	category = "adult"
else:
	category = "minor"
```

Use `elif` to check multiple mutually exclusive conditions. Python executes the first true branch and skips the rest:

```python
if score >= 90:
	grade = "A"
elif score >= 80:
	grade = "B"
elif score >= 70:
	grade = "C"
else:
	grade = "Needs improvement"
```

An `else` branch is optional, but it must be the final branch. Nested conditions are valid, although combining clear conditions or using early returns often improves readability.

## 3. Logical Operators

Logical operators combine conditions:

- `and`: both operands must be truthy.
- `or`: at least one operand must be truthy.
- `not`: reverses truthiness.

```python
has_ticket = True
age = 21
if age >= 18 and has_ticket:
	print("Entry allowed")
```

Python short-circuits evaluation. `and` stops at the first falsey operand, while `or` stops at the first truthy operand. They return an operand, not necessarily `True` or `False`:

```python
display_name = user_name or "Guest"
```

De Morgan's laws are useful when simplifying conditions:

```python
not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)
```

## 4. The `while` Loop

Use `while` when repetition depends on a condition. The body must change state so the condition eventually becomes false.

```python
counter = 3
while counter > 0:
	print(counter)
	counter -= 1
```

If the condition is false initially, the body runs zero times. An intentional infinite loop uses `while True` and must have a reachable `break`:

```python
while True:
	command = get_command()
	if command == "quit":
		break
```

Avoid accidental infinite loops by updating the loop variable or changing the state checked by the condition.

## 5. The `for` Loop and `range()`

Use `for` to iterate over an iterable such as a string, list, tuple, set, dictionary, or `range` object:

```python
for letter in "Python":
	print(letter)
```

`range()` generates integer values lazily and excludes its stop value:

```python
range(stop)
range(start, stop)
range(start, stop, step)
```

Examples:

```python
for number in range(5):       # 0, 1, 2, 3, 4
	print(number)

for number in range(6, 0, -2): # 6, 4, 2
	print(number)
```

`range()` accepts integers only. A zero step raises `ValueError`.

## 6. `break`, `continue`, and Loop `else`

- `break` exits the nearest loop immediately.
- `continue` skips the rest of the current iteration and starts the next one.
- `pass` does nothing and is useful as a temporary placeholder.

```python
for number in range(1, 10):
	if number == 5:
		break
	if number % 2 == 0:
		continue
	print(number)
```

A loop `else` runs when the loop finishes normally, including when it runs zero times. It does not run when the loop exits with `break`. This is useful for searches:

```python
for item in items:
	if item == target:
		print("Found")
		break
else:
	print("Not found")
```

## 7. Bitwise Operators

Logical operators work with whole truth values. Bitwise operators work on individual bits of integers:

| Operator | Meaning | Example |
| --- | --- | --- |
| `&` | Bitwise AND | `0b1100 & 0b1010` gives `0b1000` |
| `\|` | Bitwise OR | `0b1100 \| 0b1010` gives `0b1110` |
| `^` | Bitwise XOR | `0b1100 ^ 0b1010` gives `0b0110` |
| `~` | Bitwise NOT | `~4` gives `-5` |
| `<<` | Shift left | `4 << 1` gives `8` |
| `>>` | Shift right | `9 >> 1` gives `4` |

Bit masks select or change specific flags:

```python
READ = 0b001
WRITE = 0b010
permissions = READ | WRITE
has_write = bool(permissions & WRITE)
permissions &= ~WRITE
```

For non-negative integers, `value << bits` multiplies by $2^{bits}$ and `value >> bits` performs floor division by $2^{bits}$. Bitwise operators require integer operands.

## 8. Iterating Over Collections

Iterate over values directly when possible:

```python
numbers = [10, 1, 8, 3]
total = 0
for number in numbers:
	total += number
```

Use `enumerate()` when both the index and value are needed:

```python
for index, value in enumerate(numbers):
	print(index, value)
```

List comprehensions create a list from an iterable, optionally filtering values:

```python
squares = [number ** 2 for number in range(5)]
odd_squares = [square for square in squares if square % 2]
```

Nested comprehensions can represent a matrix, but use ordinary loops when the comprehension becomes difficult to read.

## 9. Common Algorithms

### Largest value without `max()`

```python
largest = numbers[0]
for number in numbers[1:]:
	if number > largest:
		largest = number
```

### Remove duplicates while preserving order

```python
unique = []
for item in numbers:
	if item not in unique:
		unique.append(item)
```

For production code, a `set` is usually more efficient for membership checks, provided the values are hashable.

### Validate a leap year

```python
is_leap_year = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
```

## 10. Readability Rules

- Use four spaces for indentation and never mix tabs with spaces.
- Keep conditions simple; assign complex conditions descriptive names.
- Prefer bounded loops and clear exit conditions.
- Avoid changing a collection while iterating over it unless the behavior is deliberate.
- Use `break` and `continue` when they clarify control flow, not merely to shorten code.
