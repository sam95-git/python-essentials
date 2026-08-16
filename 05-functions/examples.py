"""Runnable examples for defining and using functions."""


def greet(name, punctuation="!"):
	return f"Hello, {name}{punctuation}"


def average(numbers):
	if not numbers:
		raise ValueError("numbers must not be empty")
	return sum(numbers) / len(numbers)


def factorial(number):
	if number < 0:
		raise ValueError("number must be non-negative")
	result = 1
	for value in range(2, number + 1):
		result *= value
	return result


def collect(*numbers):
	return sum(numbers)


def describe(**fields):
	return fields


def add_item(items, item):
	items.append(item)


def main():
	print(greet("Ada"))
	print(greet(name="Grace", punctuation="."))
	print("average:", average([10, 20, 30]))
	print("factorial:", factorial(5))
	print("collect:", collect(1, 2, 3))
	print("options:", describe(language="Python", level="beginner"))
	values = []
	add_item(values, "functions")
	print("mutated list:", values)


if __name__ == "__main__":
	main()
