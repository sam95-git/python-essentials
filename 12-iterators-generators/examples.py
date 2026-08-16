"""Runnable examples for iterators and generators."""


def count_up_to(limit):
	for number in range(limit):
		yield number


def flatten(groups):
	for group in groups:
		yield from group


def squares(values):
	return (value * value for value in values)


def main():
	iterator = iter([10, 20, 30])
	print("next:", next(iterator), next(iterator))
	print("generator:", list(count_up_to(4)))
	print("flattened:", list(flatten([[1, 2], [3], [4, 5]])))
	print("squares:", list(squares(range(4))))


if __name__ == "__main__":
	main()
