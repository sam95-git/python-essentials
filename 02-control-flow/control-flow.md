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

`=` assigns a value; `==` compares two values. Equality and inequality (`==`, `!=`) have lower precedence than ordering comparisons (`<`, `<=`, `>`, `>=`), and each comparison returns `True` or `False`.

Numeric values such as `2` and `2.0` compare equal with `==`, even though one is an `int` and the other is a `float`.

```python
black_sheep == 2 * white_sheep
```

Multiplication is evaluated before equality, so this is equivalent to `black_sheep == (2 * white_sheep)`. A comparison that uses variables can only be resolved when their runtime values are known.

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

### Conditional execution patterns

- A standalone `if` is evaluated independently from other `if` statements; multiple blocks may run.
- An `if`/`elif`/`else` cascade selects at most one branch: the first true branch runs.
- `else` pairs with the nearest unmatched `if` at the same indentation level. Indentation is part of Python syntax; use consistent four-space indentation.
- Statements outside the indented block run regardless of whether the condition is true.
- Conditions use Python truthiness: `False`, `None`, numeric zero, and empty collections are falsey; most other values are truthy.

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

## 11. Worked Conditional Scenarios

### Compare a number with 100

Print `False` below 100 and `True` at or above 100. No `if` is needed because the comparison itself produces the required Boolean value.

```python
n = int(input())
print(n >= 100)
```

### Select a message for a plant name

String comparisons are case-sensitive, so the two spellings are handled as separate cases.

```python
plant = input()

if plant == "Spathiphyllum":
	print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
	print("No, I want a big Spathiphyllum!")
else:
	print(f"Spathiphyllum! Not {plant}!")
```

### Calculate personal income tax

Write a tax calculator that takes a citizen's income (float) and calculates their Personal Income Tax (PIT) based on these rules:Income $\le$ 85,528 thalers: Tax is $18\%$ of the income minus $556.02$ thalers.Income > 85,528 thalers: Tax is $14,839.02$ thalers plus $32\%$ of the surplus over $85,528$ thalers.No Refunds: If the calculated tax is less than zero, the tax is $0$.Output: Print the final tax rounded to the nearest full thaler using round().

Apply the correct bracket, clamp negative tax to zero, then round the result as requested.

```python
income = float(input())

if income <= 85_528:
	tax = 0.18 * income - 556.02
else:
	tax = 14_839.02 + 0.32 * (income - 85_528)

tax = max(0, round(tax))
print("The tax is:", float(tax), "thalers")
```

Expected examples: `10000` gives `1244.0`; `100000` gives `19470.0`; `1000` and `-100` both give `0.0`.

### Classify a Gregorian calendar year

A Gregorian leap year is divisible by 400, or divisible by 4 but not by 100. This implementation follows the supplied exercise's lower boundary of 1582.

```python
year = int(input())

if year < 1582:
	print("Not within the Gregorian calendar period")
elif year % 400 == 0:
	print("Leap year")
elif year % 100 == 0:
	print("Common year")
elif year % 4 == 0:
	print("Leap year")
else:
	print("Common year")
```

### Find the largest of two or three values

For two values, choose between the two branches. For three or more, track the best value seen so far and update it after each comparison.

```python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if number1 > number2:
	larger_number = number1
else:
	larger_number = number2

print("The larger number is:", larger_number)
```

```python
numbers = [int(input("Enter a number: ")) for _ in range(3)]
largest_number = numbers[0]

for number in numbers[1:]:
	if number > largest_number:
		largest_number = number

print("The largest number is:", largest_number)
```

## 12. Final Quiz: Interview Practice

These are the end-of-section output questions, with answers for self-checking.

### Question 1

```python
x = 5
y = 10
z = 8
 
print(x > y)
print(y > z)
```

**Answer:**

```text
False
True
```

### Question 2

```python
x, y, z = 5, 10, 8
 
print(x > z)
print((y - 5) == x)
```

**Answer:**

```text
False
True
```

### Question 3

```python
x, y, z = 5, 10, 8
x, y, z = z, y, x
 
print(x > z)
print((y - 5) == x)
```

**Answer:**

```text
True
False
```

### Question 4

```python
x = 10
 
if x == 10:
	print(x == 10)
if x > 5:
	print(x > 5)
if x < 10:
	print(x < 10)
else:
	print("else")
```

**Answer:**

```text
True
True
else
```

The `else` belongs to the third `if`, because it is aligned with that `if`.

### Question 5

```python
x = "1"
 
if x == 1:
	print("one")
elif x == "1":
	if int(x) > 1:
		print("two")
	elif int(x) < 1:
		print("three")
	else:
		print("four")
if int(x) == 1:
	print("five")
else:
	print("six")
```

**Answer:**

```text
four
five
```

### Question 6

```python
x = 1
y = 1.0
z = "1"
 
if x == y:
	print("one")
if y == int(z):
	print("two")
elif x == y:
	print("three")
else:
	print("four")
```

**Answer:**

```text
one
two
```

`1 == 1.0` is true, and `int("1")` converts the string to the integer `1`.
