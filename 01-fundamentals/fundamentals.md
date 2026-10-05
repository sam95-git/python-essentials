# Python Fundamentals

Quick revision notes for Python's basic syntax, output, literals, operators, variables, comments, and user input.

## 1. Instructions and Console Output

- A **program** is a sequence of instructions. Each instruction performs an action when executed.
- `print()` is a **built-in function** that writes values to the console. Built-in functions are available without importing them.
- A **function call** (or invocation) uses the function name followed by parentheses. Arguments go inside the parentheses and are separated by commas.
- Calling `print()` with no arguments prints a blank line. `print()` returns `None`; its main purpose is its output side effect.
- Python strings are enclosed in matching single or double quotes.
- Inside strings, the backslash introduces an **escape sequence**. For example, `\n` represents a newline.
- **Positional arguments** are interpreted by their order. **Keyword arguments** are identified by parameter names.
- `print()`'s `sep` parameter controls the separator between arguments (default: a space); `end` controls what is written after them (default: a newline).


### Examples

```python
print("My\nname\nis\nBond.", end=" ")
print("James Bond.")

print(sep="&", "fish", "chips")
```

**Interview note:** In a function call, positional arguments must come before keyword arguments. The final call above places positional arguments after a keyword argument, so it raises `SyntaxError` as written.

## 2. Literals and Built-in Value Types

- A **literal** is a fixed value written directly in source code, such as `123`, `2.0`, `"hello"`, `True`, or `None`.
- An **integer** (`int`) has no fractional part. A **floating-point number** (`float`) represents values with a fractional component.
- Numeric bases include:

| Base | Name | Digits / notation | Example |
| --- | --- | --- | --- |
| 2 | Binary | `0`, `1` | `0b1010` is decimal `10` |
| 8 | Octal | `0`–`7` | `0o12` is decimal `10` |
| 10 | Decimal | `0`–`9` | `10` |
| 16 | Hexadecimal | `0`–`9`, `A`–`F` | `0xA` is decimal `10` |

- `True` and `False` are the two **Boolean** values. In numeric contexts, `True` behaves like `1` and `False` like `0`.
- `None` is the singleton value of type `NoneType`; it represents the **absence of a value**. Check it with `is None`.
- To include a quote or apostrophe inside a string, escape it with `\` or delimit the string with the other quote style.

### Examples and Quick Checks

What types of literals are the following four examples?

```
"1.5", 2.0, 528, False
```

What is the decimal value of the following binary number?

```
1011
```

## 3. Expressions and Operators

- An **expression** combines values, variables, operators, and function calls, and evaluates to a value.
- An **operator** performs an operation on one or more operands.
- A **unary operator** has one operand; a **binary operator** has two.

### Arithmetic Operators

| Operator | Purpose | Key behavior |
| --- | --- | --- |
| `**` | Exponentiation | Raises the left operand to the power of the right operand |
| `+` | Addition / unary plus | Adds two values; unary plus preserves a number's sign |
| `-` | Subtraction / unary minus | Subtracts values; unary minus negates a number |
| `*` | Multiplication | Multiplies values; also repeats strings/sequences |
| `/` | True division | Always returns a `float` |
| `//` | Floor division | Rounds the quotient down toward negative infinity |
| `%` | Modulo | Returns the remainder after division |

### Operator Precedence

For the operators covered here, higher-priority operations are evaluated first. Parentheses can explicitly control the order.

| Priority (high to low) | Operators | Associativity / notes |
| --- | --- | --- |
| 1 | Parenthesized expressions `( … )` | Evaluate the parenthesized expression first |
| 2 | `**` | Right-associative: `2 ** 2 ** 3` means `2 ** (2 ** 3)` |
| 3 | Unary `+`, unary `-` | A unary operator on the right of `**` is allowed in the exponent: `4 ** -1` is `0.25`; a leading minus applies after exponentiation: `-3 ** 2` is `-(3 ** 2)` |
| 4 | `*`, `/`, `//`, `%` | Same precedence; evaluate left to right |
| 5 | Binary `+`, binary `-` | Same precedence; evaluate left to right |

**Interview reminders:**

- `2 ** 3 ** 2` is `2 ** (3 ** 2)`, or `512`.
- `//` is floor division, not truncation toward zero: `-3 // 2` is `-2`.
- Parentheses are useful both to override precedence and to make intent clear.

### Examples and Output Questions

What is the expected output of the following snippet?

```python
print((2 ** 4), (2 * 4.), (2 * 4))
```

What is the expected output of the following snippet?

```python
print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
```

What is the expected output of the following snippet?

```python
print((2 % -4), (2 % 4), (2 ** 3 ** 2))
```

## 4. Variables, Identifiers, and Assignment

- A **variable** is a name bound to an object. Assignment creates the binding the first time and rebinds it later.
- Python is **dynamically typed**: names do not need type declarations and can be rebound to objects of different types.
- A valid **identifier** starts with a letter or underscore, followed by letters, digits, or underscores. Identifiers are case-sensitive and cannot be Python keywords.
- Use `=` for assignment; it does not mean equality. Use `==` to compare values.
- **Augmented assignment** combines an operation with assignment, such as `+=`, `/=`, and `*=`.
- Prefer descriptive, self-documenting `snake_case` names. Avoid shadowing built-in names such as `list` or `print`.

### Examples and Output Questions

```python
var = 2
print(var)

var = 3
print(var)

var += 1
print(var)
```

You can combine text and variables using the + operator, and use the print() function to output strings and variables, for example:

```python
var = "007"
print("Agent " + var)
```

What is the output of the following snippet?

```python
a = '1'
b = "1"
print(a + b)
```

What is the output of the following snippet?

```python
a = 6
b = 3
a /= 2 * b
print(a)
```

## 5. Comments and Readable Code

- A comment begins with `#` and continues to the end of the line. Comments are for readers and are ignored during normal execution.
- For a multi-line comment, prefix each line with `#`.
- Use comments to explain intent or non-obvious decisions; keep them accurate and avoid restating obvious code.
- Readable variable names and focused comments help both future-you and other developers understand the code.

### Example

```python
# This program prints
# an introduction to the screen.
print("Hello!")  # Invoking the print() function
# print("I'm Python.")
```

## 6. Console Input and String Operations

- `print()` sends data to the console; `input()` reads a line from the console.
- `input()` may take a prompt string, displayed before input is read.
- `input()` always returns a `str`. Convert the result with `int()` or `float()` before numeric calculations.
- `+` concatenates strings; `*` repeats a string by an integer count.
- `input()` pauses the program until the user submits input. An empty `input()` call can wait for the user to press Enter.

### Examples

```python
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")
```

```python
name = input("Enter your name: ")
print("Hello, " + name + ". Nice to meet you!")

print("\nPress Enter to end the program.")
input()
print("THE END.")
```

```python
num_1 = input("Enter the first number: ") # Enter 12
num_2 = input("Enter the second number: ") # Enter 21

print(num_1 + num_2) # the program returns 1221
```

```python
my_input = input("Enter something: ") # Example input: hello
print(my_input * 3) # Expected output: hellohellohello
```

### Output Questions

What is the output of the following snippet?

```python
x = int(input("Enter a number: ")) # The user enters 2
print(x * "5")
```

What is the expected output of the following snippet?

```python
x = input("Enter a number: ") # The user enters 2
print(type(x))
```
