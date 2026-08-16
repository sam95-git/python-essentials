# Functions: Interview Preparation

## Core Questions

### 1. What is the difference between a parameter and an argument?

A parameter is a variable listed in a function definition. An argument is the actual value passed during a call.

### 2. What does a function return by default?

`None`, when execution reaches the end without an expression in a `return` statement.

### 3. Why are mutable default arguments dangerous?

Default values are created once when the function is defined, not on every call. A list default can therefore retain values between calls. Use `None` and initialize inside the function.

### 4. Is Python pass-by-value or pass-by-reference?

Python uses pass-by-assignment: a parameter receives a reference to the same object. Rebinding the parameter is local, while mutating the referenced mutable object is observable by the caller.

### 5. What is LEGB?

The name lookup order is Local, Enclosing, Global, and Built-in.

### 6. What are `*args` and `**kwargs`?

`*args` collects extra positional arguments as a tuple. `**kwargs` collects extra keyword arguments as a dictionary.

### 7. What makes a good function?

It has one clear responsibility, a descriptive name, a small interface, predictable inputs and outputs, limited side effects, and tests for normal and boundary cases.

## Output Questions

```python
def add_item(items=[]):
	items.append(1)
	return items

print(add_item())
print(add_item())
```

**Answer:** `[1]` followed by `[1, 1]`. The default list is shared.

```python
def update(value):
	value += 1

number = 5
update(number)
print(number)
```

**Answer:** `5`; integer rebinding inside the function does not change the caller's name.

```python
def choose(value):
	if value > 0:
		return "positive"

print(choose(0))
```

**Answer:** `None`.

## Common Traps

- Defining a function does not call it.
- Positional arguments cannot follow keyword arguments.
- `return print(value)` returns `None` because `print()` returns `None`.
- Avoid shadowing built-ins such as `list`, `sum`, and `input`.
- Recursion requires a reachable base case.
- Type hints document intent but do not enforce types at runtime.

## Practice

1. Write `is_prime(number)` returning a Boolean.
2. Write `days_in_month(year, month)` returning `None` for invalid input.
3. Implement iterative and recursive factorial functions.
4. Refactor a repeated calculation into a pure function.
