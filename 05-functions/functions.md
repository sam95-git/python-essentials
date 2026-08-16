# Python Functions

Functions package a focused task into a reusable block. They reduce duplication, support decomposition, and make code easier to test.

## 1. Define and Call a Function

```python
def greet():
	print("Hello, Python!")

greet()
```

Python must execute a function definition before the function is called. The indented body belongs to the function.

## 2. Parameters and Arguments

Parameters are names in a function definition. Arguments are values supplied by the caller.

```python
def greet(name, punctuation="!"):
	return f"Hello, {name}{punctuation}"

print(greet("Ada"))
print(greet(name="Grace", punctuation="."))
```

Positional arguments must come before keyword arguments. Default parameters make arguments optional. Avoid mutable defaults such as `items=[]`; use `None` and create the list inside the function.

## 3. Return Values

`return` ends the function and sends a value to the caller. A function without an explicit return value returns `None`.

```python
def add(first, second):
	return first + second

result = add(2, 3)
```

Printing a result and returning a result are different responsibilities: `print()` displays a value, while `return` makes it available to other code.

## 4. Scope and Arguments

Local variables exist inside the function. Names are resolved using the local, enclosing, global, and built-in scopes (LEGB). Reading a global name is possible, but avoid modifying global state. Use `global` only when it is genuinely required.

Python passes object references by assignment. Rebinding a parameter does not rebind the caller's name, but mutating a mutable object can be visible to the caller.

```python
def add_item(items, item):
	items.append(item)  # mutates the shared list

values = []
add_item(values, "Python")
```

## 5. Flexible Arguments

`*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dictionary.

```python
def total(*numbers):
	return sum(numbers)

def show_options(**options):
	return options
```

Use keyword-only parameters after `*` when clarity matters:

```python
def connect(host, *, timeout=5):
	return host, timeout
```

## 6. Recursion and Documentation

A recursive function calls itself and must have a base case. Recursion can express tree-like problems clearly, but deep recursion can hit Python's recursion limit; iteration is often more efficient.

```python
def factorial(number):
	if number < 0:
		raise ValueError("number must be non-negative")
	if number < 2:
		return 1
	return number * factorial(number - 1)
```

Use a docstring to describe a public function's purpose, parameters, return value, and errors. Keep functions small, focused, and easy to test.
