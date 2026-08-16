# Python Object-Oriented Programming

Object-oriented programming models state and behavior together in objects. Python also supports procedural and functional styles; choose the style that fits the problem.

## 1. Classes and Instances

A class defines behavior and an instance holds object-specific state.

```python
class Account:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		self.balance += amount
```

`self` refers to the current instance. `__init__` initializes an already-created instance; it is not the constructor itself in the strict language sense.

## 2. Encapsulation and Properties

Python uses conventions rather than enforced private fields. A leading underscore signals internal use. Double underscores trigger name mangling.

Properties provide validated attribute access:

```python
class Temperature:
	def __init__(self, celsius):
		self.celsius = celsius

	@property
	def celsius(self):
		return self._celsius

	@celsius.setter
	def celsius(self, value):
		if value < -273.15:
			raise ValueError("below absolute zero")
		self._celsius = value
```

## 3. Inheritance and Polymorphism

Inheritance models an is-a relationship. A subclass can override methods and use `super()` to reuse parent behavior.

```python
class Animal:
	def speak(self):
		raise NotImplementedError

class Dog(Animal):
	def speak(self):
		return "woof"
```

Duck typing focuses on supported behavior rather than exact class. Prefer composition over inheritance when objects do not share a true conceptual relationship.

## 4. Special Methods and Dataclasses

Special methods customize built-in operations, such as `__repr__`, `__eq__`, `__len__`, and `__iter__`. `@dataclass` generates common boilerplate for data-focused classes.

```python
from dataclasses import dataclass

@dataclass
class Point:
	x: float
	y: float
```

Class attributes are shared by instances; instance attributes belong to one object. Avoid mutable class attributes when each instance should have independent state.

## 5. Design Principles

- Keep each class focused.
- Validate invariants at boundaries.
- Prefer clear public methods over direct state manipulation.
- Use composition and dependency injection for flexible design.
- Implement equality and hashing consistently.
