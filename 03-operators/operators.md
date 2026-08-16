# Python Operators and User Interaction

An operator performs an operation on one or more operands. Values, variables, function calls, and operators combine to form expressions.

## 1. Arithmetic Operators

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | Addition | `7 + 2` | `9` |
| `-` | Subtraction | `7 - 2` | `5` |
| `*` | Multiplication | `7 * 2` | `14` |
| `/` | True division | `7 / 2` | `3.5` |
| `//` | Floor division | `7 // 2` | `3` |
| `%` | Remainder | `7 % 2` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

`/` always returns a float. `//` rounds down toward negative infinity, so `-7 // 2` is `-4`, not `-3`. Division, floor division, and modulo by zero raise `ZeroDivisionError`.

`+` and `-` can also be unary operators:

```python
temperature = -5
print(+temperature, -temperature)
```

For strings, `+` concatenates and `*` repeats:

```python
print("Py" + "thon")
print("ha" * 3)
```

## 2. Comparison Operators

Comparisons return `True` or `False`:

```python
age = 20
print(age >= 18)
print(age == 20)
print(age != 21)
```

Operators are `==`, `!=`, `<`, `<=`, `>`, and `>=`. Chained comparisons are readable and evaluated as a combined condition:

```python
if 0 <= score <= 100:
	print("Valid score")
```

## 3. Logical Operators

- `and` is true when both conditions are true.
- `or` is true when at least one condition is true.
- `not` reverses truthiness.

Python short-circuits these operators. It also returns an operand, not necessarily a Boolean:

```python
username = user_input or "Guest"
is_ready = has_data and is_valid
```

Use parentheses when they make a condition clearer.

## 4. Assignment Operators

`=` assigns a value. Compound assignment updates a variable using its current value:

```python
total = 10
total += 5
total *= 2
total //= 3
total %= 4
```

Available forms include `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`, and bitwise variants such as `&=`.

## 5. Membership, Identity, and Bitwise Operators

`in` and `not in` test membership:

```python
print("py" in "python")
print(3 not in [1, 2])
```

`is` and `is not` test whether two names refer to the same object. Use them mainly with `None`:

```python
value = None
print(value is None)
```

Bitwise operators work on integer bits: `&` (and), `|` (or), `^` (xor), `~` (invert), `<<` (left shift), and `>>` (right shift).

## 6. Precedence and Associativity

Parentheses are evaluated first. A useful simplified order is:

1. Parentheses
2. Exponentiation: `**`
3. Unary `+`, unary `-`, and `~`
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. Comparisons, `in`, `is`
7. `not`, then `and`, then `or`

Most operators associate from left to right. Exponentiation associates from right to left:

```python
print(2 ** 3 ** 2)
print(-2 ** 2)
print((-2) ** 2)
```

Prefer parentheses when intent is not obvious.

## 7. Reading User Input

`input()` displays an optional prompt, waits for a line, and always returns a string. Convert it before arithmetic:

```python
name = input("Name: ")
age = int(input("Age: "))
print(f"{name} will be {age + 1} next year.")
```

For robust programs, catch invalid numeric input:

```python
try:
	amount = float(input("Amount: "))
except ValueError:
	print("Please enter a valid number.")
```

Never use `eval(input(...))` for ordinary user input. It can execute arbitrary Python code. Parse only the type and format the program expects.

## 8. Useful Expressions

```python
minutes = 135
hours, remaining_minutes = divmod(minutes, 60)
print(hours, remaining_minutes)

number = 12
print("even" if number % 2 == 0 else "odd")
```
