# Control Flow: Interview Preparation

## Core Questions

### 1. What is the difference between `if`, `elif`, and multiple `if` statements?

An `if`/`elif`/`else` cascade selects at most one branch: after the first true condition, the remaining branches are skipped. Separate `if` statements are all evaluated independently, so multiple blocks may run.

### 2. What is the difference between `break`, `continue`, and `pass`?

`break` terminates the nearest loop, `continue` skips the current iteration, and `pass` performs no action. `pass` does not skip an iteration or exit a loop.

### 3. When does a loop's `else` block execute?

It executes when the loop completes normally, including an empty iteration sequence. It does not execute when `break` terminates the loop. This makes it useful for search code.

### 4. What is the difference between `while` and `for`?

`while` repeats while a condition remains true and is suitable when the number of repetitions is unknown. `for` iterates over an iterable and is suitable when processing each item or a known range.

### 5. What does `range(2, 10, 3)` produce?

It produces `2, 5, 8`. The start is included, the stop is excluded, and the step is `3`.

### 6. What causes an infinite `while` loop?

The condition remains truthy because the loop body does not update the relevant state, updates it in the wrong direction, or has an unreachable exit. Every loop should have a demonstrably reachable termination path.

### 7. How do logical operators short-circuit?

`and` stops at the first falsey operand; `or` stops at the first truthy operand. This can avoid unnecessary work or protect an expression such as `items and items[0]`.

### 8. How are logical and bitwise operators different?

`and`, `or`, and `not` evaluate truthiness and return Boolean-style logical results or operands. `&`, `|`, `^`, and `~` operate on individual bits and require integer operands.

### 9. What does `~x` mean for integers?

Python integers use signed two's-complement semantics for bitwise inversion, so `~x == -x - 1`. Therefore, `~4` is `-5`.

### 10. What is the risk of deeply nested conditionals?

They make execution paths difficult to read and test. Guard clauses, descriptive Boolean variables, and small functions can reduce nesting while preserving behavior.

## Output-Based Questions

### Question 1

```python
x = 10
if x > 5:
	print("A")
if x > 8:
	print("B")
else:
	print("C")
```

**Answer:**

```text
A
B
```

The `else` belongs to the second `if`, not the first one.

### Question 2

```python
for number in range(5):
	if number == 3:
		break
else:
	print("complete")
print(number)
```

**Answer:** `3`. The loop ended through `break`, so its `else` block was skipped.

### Question 3

```python
value = 0
while value < 3:
	value += 1
else:
	print(value)
```

**Answer:** `3`. The condition became false naturally, so the `else` block ran.

### Question 4

```python
p = 15
q = 22
print(p and q)
print(p & q)
print(p ^ q)
```

**Answer:**

```text
22
6
25
```

`and` returns the second truthy operand. The other operators work bit by bit.

### Question 5

```python
for number in range(1, 6):
	if number % 2 == 0:
		continue
	print(number, end=" ")
```

**Answer:** `1 3 5 `.

## Common Traps

- `=` assigns; `==` compares.
- `range()` excludes the stop value.
- `range(5, 0)` is empty because the default step is positive; use `range(5, 0, -1)` to count down.
- A loop `else` is not an `if` attached to the last iteration; it depends on whether `break` occurred.
- `and` and `or` return operands, so their result may be a string, number, or object.
- `not` has higher precedence than `and`, which has higher precedence than `or`; parentheses improve clarity.
- `continue` in a `while` loop must not skip the state update needed for termination.
- `~4` is `-5`, not `-4`.
- Bitwise operators do not replace logical operators for ordinary conditions.

## Practice Problems

1. Implement the Spathiphyllum message exercise using `if`/`elif`/`else`.
2. Write a leap-year validator that rejects years before 1582.
3. Build a number-guessing loop that exits with `break` when the guess is correct.
4. Write a vowel eater using `for` and `continue`, then rewrite it using a list comprehension.
5. Implement the Collatz sequence and count its steps until it reaches `1`.
6. Find the largest item in a list without using `max()`.
