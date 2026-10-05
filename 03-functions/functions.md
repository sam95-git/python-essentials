# Python Functions

Functions package a focused task into a reusable block. They reduce duplicated code, support decomposition, and make behavior easier to understand and test.

## Why Functions Matter

- **Reuse:** define repeated logic once and call it wherever needed.
- **Decomposition:** break a large problem into smaller, independently understandable pieces.
- **Maintenance:** one change to a shared function updates every call site.
- **Collaboration:** teams can implement separate functions or modules with clear responsibilities.
- **Testing:** focused functions are easier to test with known inputs and expected outputs.

Prefer short functions with one clear purpose. A useful function name describes the action or result.

## Where Functions Come From

- **Built-ins:** always available, such as `print()`, `input()`, `len()`, and `max()`.
- **Standard-library modules:** available after importing a module, such as `sqrt()` from `math`.
- **User-defined functions:** written in project code with `def`.
- Functions are also available through classes as methods; methods are called through an object or class.

## Defining and Calling Functions

Use `def`, a function name, parentheses, and a colon. The indented body runs when the function is called, not when it is merely defined.

```python
def message():
    print("Enter a value:")

print("We start here.")
message()
print("We end here.")
```

The function must be bound to its name before execution reaches a call to it. Avoid reusing a function name for a variable; rebinding that name makes the function inaccessible through it.

## Parameters and Arguments

- A **parameter** is a name in the function definition.
- An **argument** is a value supplied by the caller.
- A parameter is local to its function. It is initialized from the corresponding argument when called.
- The number and names of supplied arguments must match the function's parameters unless defaults or flexible arguments are provided.

```python
def introduce(first_name, last_name="Smith"):
    return f"Hello, my name is {first_name} {last_name}."

print(introduce("Ada"))
print(introduce(last_name="Lovelace", first_name="Ada"))
```

### Argument-passing styles

- **Positional:** values bind by order, e.g. `subtract(9, 4)`.
- **Keyword:** values bind by parameter name, e.g. `subtract(first=9, second=4)`; their order can vary.
- **Mixed:** positional arguments must come before keyword arguments. Do not provide a parameter more than once.
- **Default values:** make parameters optional. Parameters with defaults must follow required parameters.

### `*args` and `**kwargs`

Use these conventional parameter names when a function needs to accept a variable number of arguments:

- `*args` collects any extra **positional arguments** into a tuple. The name `args` is a convention; the `*` is what performs the collection.
- `**kwargs` collects any extra **keyword arguments** into a dictionary. The name `kwargs` is a convention; the `**` performs the collection.
- They are useful for forwarding arguments, writing flexible utility functions, and wrapping other callables. Prefer explicit parameters when the expected inputs are known, because they make the function easier to understand.
- In a function signature, parameters are typically ordered as required parameters, `*args`, keyword-only parameters, and finally `**kwargs`.

```python
def show_arguments(*args, **kwargs):
    print("positional:", args)
    print("keyword:", kwargs)


show_arguments("red", "blue", size="large", available=True)
```

Output:

```text
positional: ('red', 'blue')
keyword: {'size': 'large', 'available': True}
```

The same `*` and `**` syntax can **unpack** an iterable or mapping when calling a function:

```python
def introduce(first_name, last_name):
    return f"{first_name} {last_name}"


names = ("Ada", "Lovelace")
details = {"first_name": "Grace", "last_name": "Hopper"}

print(introduce(*names))
print(introduce(**details))
```

Here, `*names` supplies two positional arguments and `**details` supplies named arguments. Dictionary keys must match the function's parameter names.

Default values are evaluated once when the function is defined. For a mutable default, use `None` and create a new object inside the function.

```python
def collect(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## Return Values and Side Effects

- `return expression` ends the call and passes the evaluated value back to the caller.
- `return` without an expression also ends the call, returning `None`.
- Reaching the end of a function without `return` also returns `None`.
- `print()` displays a value; it does not return that displayed value. Use `return` when callers need to use a result.
- A function may have side effects, such as printing or mutating an object, as well as a return value.

```python
def add(first, second):
    return first + second

result = add(2, 3)
```

## Scope and State

**Scope** is the part of a program where a name can be accessed. Python looks up names in **LEGB** order:

1. **Local:** names assigned inside the current function, including its parameters.
2. **Enclosing:** names in surrounding functions, for nested functions.
3. **Global:** names defined at the module level.
4. **Built-in:** names provided by Python, such as `len` and `print`.

### Local names and shadowing

A local name is available only in its function. A local name can have the same spelling as a global name; it then **shadows** the global name within that function. The function must be called before its local variables are created, and those locals cannot be accessed outside the function.

```python
value = 10

def show_local_value():
    value = 20
    print("inside:", value)


show_local_value()
print("outside:", value)
```

Output:

```text
inside: 20
outside: 10
```

### Reading and rebinding global names

A function can read a global name. If you assign to that name inside the function, Python treats it as local unless you declare it `global` first. Prefer passing a value in and returning the updated value; this makes dependencies explicit and is easier to test.

```python
count = 1

def increment_local():
    count = 2
    return count


def increment_global():
    global count
    count += 1
    return count


print(increment_local(), count)
print(increment_global(), count)
```

Output:

```text
2 1
2 2
```

`increment_local()` creates a local `count` and leaves the module-level value alone. `increment_global()` uses the module-level name because of the `global` declaration.

### Parameter binding, rebinding, and mutation

Python passes **object references by assignment**: a parameter becomes another local name for the object passed by the caller.

- Rebinding a parameter changes only the local name; it does not rebind the caller's variable.
- Mutating a shared mutable object, such as a list, changes that object and is visible to the caller.
- Rebinding the parameter to a new list does not change what the caller's variable refers to.

```python
def rebind_number(number):
    number = 99


def rebind_list(items):
    items = ["new list"]


def mutate_list(items):
    items.append("added by function")


number = 5
values = ["original"]

rebind_number(number)
rebind_list(values)
print(number, values)

mutate_list(values)
print(number, values)
```

Output:

```text
5 ['original']
5 ['original', 'added by function']
```

Use mutation intentionally. If callers should keep their original collection unchanged, make and return a copy instead of modifying the shared object.

### Nested functions and `nonlocal`

A nested function can read a name from its enclosing function. Use `nonlocal` to rebind that enclosing name; it does not refer to a module-level global.

```python
def make_counter():
    count = 0

    def next_value():
        nonlocal count
        count += 1
        return count

    return next_value


counter = make_counter()
print(counter(), counter())
```

Output: `1 2`.

## Worked Function Examples

### Days in a month and day of a year

Return `None` when the year, month, or day is invalid. February depends on the leap-year rule.

```python
def is_year_leap(year):
    return year > 0 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))


def days_in_month(year, month):
    if year <= 0 or not 1 <= month <= 12:
        return None

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_year_leap(year):
        return 29
    return month_lengths[month - 1]


def day_of_year(year, month, day):
    month_length = days_in_month(year, month)
    if month_length is None or not 1 <= day <= month_length:
        return None

    return sum(days_in_month(year, earlier_month) for earlier_month in range(1, month)) + day


print(days_in_month(1900, 2))  # 28
print(days_in_month(2000, 2))  # 29
print(day_of_year(2000, 12, 31))  # 366
```

### Prime-number check

A prime is an integer greater than 1 with no positive divisors other than 1 and itself. It is sufficient to test candidate divisors through the square root.

```python
def is_prime(number):
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2

    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


for number in range(1, 20):
    if is_prime(number):
        print(number, end=" ")
print()
```

Expected output: `2 3 5 7 11 13 17 19`.

### BMI and unit conversions

BMI is weight in kilograms divided by height in metres squared. Validate inputs at the function boundary; helper functions keep unit conversions reusable.

```python
def pounds_to_kilograms(pounds):
    return pounds * 0.45359237


def feet_inches_to_metres(feet, inches=0.0):
    return feet * 0.3048 + inches * 0.0254


def bmi(weight_kg, height_m):
    if weight_kg <= 0 or height_m <= 0:
        return None
    return weight_kg / height_m ** 2


print(bmi(pounds_to_kilograms(176), feet_inches_to_metres(5, 7)))
```

### Triangle checks and area

Three positive lengths form a triangle when the sum of every pair is greater than the remaining side. Heron's formula uses semi-perimeter $s=(a+b+c)/2$ and area $\sqrt{s(s-a)(s-b)(s-c)}$.

```python
from math import isclose, sqrt


def is_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and c + a > b


def is_right_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return False
    first, second, hypotenuse = sorted((a, b, c))
    return isclose(first ** 2 + second ** 2, hypotenuse ** 2, rel_tol=1e-9, abs_tol=1e-9)


def triangle_area(a, b, c):
    if not is_triangle(a, b, c):
        return None
    semi_perimeter = (a + b + c) / 2
    return sqrt(
        semi_perimeter
        * (semi_perimeter - a)
        * (semi_perimeter - b)
        * (semi_perimeter - c)
    )


print(is_triangle(1, 1, 1))
print(is_right_triangle(3, 4, 5))
print(triangle_area(3, 4, 5))
```

Floating-point calculations can produce tiny representation differences; use a tolerance such as `math.isclose()` rather than exact equality for approximate numeric results.

### Factorial and Fibonacci

An iterative factorial multiplies the integers from 2 through `n`. The Fibonacci sequence starts with 1, 1; each next value is the sum of the previous two.

```python
def factorial(number):
    if number < 0:
        return None
    product = 1
    for factor in range(2, number + 1):
        product *= factor
    return product


def fibonacci(position):
    if position < 1:
        return None
    first, second = 1, 1
    for _ in range(3, position + 1):
        first, second = second, first + second
    return first if position == 1 else second


print(factorial(5))  # 120
print([fibonacci(position) for position in range(1, 8)])
```

## Recursion

**Recursion** is when a function calls itself. Every recursive function needs a reachable **base case** to stop further calls. Recursion can make tree-shaped problems clear, but deep or repeated calls can consume significant time and stack space; iteration is often more efficient.

```python
def factorial_recursive(number):
    if number < 0:
        return None
    if number < 2:
        return 1
    return number * factorial_recursive(number - 1)
```

The naive recursive Fibonacci implementation has repeated work and exponential time complexity; use the iterative version above for practical calculation.

## Function Design Checklist

- Give each function one clear responsibility and a descriptive name.
- Keep dependencies explicit through parameters rather than hidden global state.
- Return values for callers to use; print only when console output is the intended effect.
- Validate inputs and document the behavior for invalid values.
- Test ordinary values, boundaries, and invalid cases.
- Add a docstring to explain a public function's purpose, arguments, return value, and exceptions.

## Final Quiz: Interview Practice

Only the supplied end-of-section quiz questions are included here. Each answer is directly below its question.

### Section 1

**1. Is `input()` user-defined or built-in?**

**Answer:** It is a built-in function.

**2. What happens when a function is called before its definition has executed?**

```python
hi()
def hi():
    print("hi!")
```

**Answer:** `NameError`, because `hi` is not yet bound when Python reaches the call.

**3. What happens when this code runs?**

```python
def hi():
    print("hi")

hi(5)
```

**Answer:** `TypeError`, because `hi()` accepts no arguments but receives one.

### Section 2

**1. What is the output?**

```python
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()
```

**Answer:** `My name is Bond. James Bond.`

**2. What is the output?**

```python
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")
```

**Answer:** `My name is Sean Connery. James Bond.`

**3. What is the output?**

```python
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
```

**Answer:** `My name is Bond. Susan.`

**4. What happens when this code is parsed?**

```python
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
```

**Answer:** `SyntaxError`: a required parameter (`c`) cannot follow a parameter with a default (`b`).

### Section 3

**1. What is the output?**

```python
def hi():
    return
    print("Hi!")

hi()
```

**Answer:** No output. `return` ends the function before `print()`.

**2. What is the output?**

```python
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(is_int("5"))
```

**Answer:** `True`, `False`, then `None`. The string case reaches the end without an explicit return.

**3. What is the output?**

```python
def even_num_lst(ran):
    lst = []
    for num in range(ran):
        if num % 2 == 0:
            lst.append(num)
    return lst

print(even_num_lst(11))
```

**Answer:** `[0, 2, 4, 6, 8, 10]`.

**4. What is the output?**

```python
def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

foo = [1, 2, 3, 4, 5]
print(list_updater(foo))
```

**Answer:** `[1, 4, 9, 16, 25]`. The loop rebinds its local `elem` name and builds a new list; it does not modify the input list's elements.

### Section 4

**1. What happens when this code runs?**

```python
def message():
    alt = 1
    print("Hello, World!")

print(alt)
```

**Answer:** `NameError`; `alt` is local to `message()` and the function was not called.

**2. What is the output?**

```python
a = 1

def fun():
    a = 2
    print(a)

fun()
print(a)
```

**Answer:** `2`, then `1`. The function's local `a` shadows the global name.

**3. What is the output?**

```python
a = 1

def fun():
    global a
    a = 2
    print(a)

fun()
a = 3
print(a)
```

**Answer:** `2`, then `3`.

**4. What is the output?**

```python
a = 1

def fun():
    global a
    a = 2
    print(a)

a = 3
fun()
print(a)
```

**Answer:** `2`, then `2`; `fun()` updates the global `a`.

### Section 5

**1. What happens when this code runs, and why?**

```python
def factorial(n):
    return n * factorial(n - 1)

print(factorial(4))
```

**Answer:** It eventually raises `RecursionError`. There is no base case, so recursive calls never stop.

**2. What is the output?**

```python
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)

print(fun(25))
```

**Answer:** `56`: the calls return `25 + 28 + 3`.