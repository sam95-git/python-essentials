# Object-Oriented Programming: Interview Preparation

## Core Questions

### 1. Class versus instance?

A class is a template describing attributes and behavior. An instance is a concrete object created from that class.

### 2. What is `self`?

It is the conventional first parameter of an instance method and refers to the object on which the method was called.

### 3. What is inheritance?

It lets a subclass reuse or specialize a parent class's behavior. Use it for a genuine is-a relationship.

### 4. What is polymorphism?

Different objects can respond to the same operation according to their own implementation. Python commonly achieves this through duck typing.

### 5. Why use `@property`?

It exposes method logic through attribute syntax, useful for validation, computed values, and preserving an API while changing internal storage.

### 6. Why can mutable class attributes be dangerous?

They are shared by every instance unless shadowed, so one instance can unexpectedly modify another's state.

## Output Questions

```python
class Counter:
	value = 0
	def __init__(self):
		self.value += 1

a = Counter()
b = Counter()
print(Counter.value, a.value, b.value)
```

**Answer:** `0 1 1`; augmented assignment creates instance attributes from the class value.

```python
class Parent:
	def speak(self):
		return "parent"

class Child(Parent):
	def speak(self):
		return "child"

print(Child().speak())
```

**Answer:** `child`.

## Common Traps

- `__init__` initializes; `__new__` controls instance creation.
- Methods need `self` in the definition, but callers do not pass it explicitly.
- Inheritance does not automatically copy mutable state safely.
- `isinstance()` is usually preferable to checking exact types.
- Defining `__eq__` can affect hashability; do not create inconsistent hash behavior.

## Practice

1. Build a `BankAccount` with deposit, withdraw, and validation.
2. Create a `Shape` hierarchy with a common area interface.
3. Refactor inheritance into composition and compare the designs.
4. Add a dataclass for an immutable point record.
