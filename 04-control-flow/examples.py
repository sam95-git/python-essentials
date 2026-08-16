"""Runnable examples for conditions, loops, logical operators, and bitwise work."""


def comparison_examples():
	score = 82
	print("equal:", score == 82)
	print("passing:", score >= 50)
	print("valid:", 0 <= score <= 100)


def grade_score(score):
	if not 0 <= score <= 100:
		return "Invalid score"
	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	return "Needs improvement"


def loop_examples():
	counter = 3
	while counter:
		print("while:", counter)
		counter -= 1

	for number in range(1, 6):
		if number % 2 == 0:
			continue
		print("odd:", number)

	for number in range(1, 4):
		print("searching:", number)
	else:
		print("loop completed without break")


def find_item(items, target):
	for index, item in enumerate(items):
		if item == target:
			return index
	return -1


def largest_value(numbers):
	if not numbers:
		raise ValueError("numbers must not be empty")
	largest = numbers[0]
	for number in numbers[1:]:
		if number > largest:
			largest = number
	return largest


def collatz_sequence(start):
	if start <= 0:
		raise ValueError("start must be a positive integer")
	values = []
	current = start
	while current != 1:
		values.append(current)
		current = current // 2 if current % 2 == 0 else 3 * current + 1
	values.append(1)
	return values


def logical_and_bitwise_examples():
	first, second = 15, 22
	print("logical and:", first and second)
	print("bitwise and:", first & second)
	print("bitwise or:", first | second)
	print("bitwise xor:", first ^ second)
	print("bitwise not:", ~first)
	print("shifts:", 17 << 2, 17 >> 1)

	write = 0b010
	permissions = 0b011
	print("has write permission:", bool(permissions & write))


def list_iteration_examples():
	numbers = [10, 1, 8, 3, 1]
	print("total:", sum(numbers))
	print("squares:", [number ** 2 for number in range(5)])
	print("odd values:", [number for number in numbers if number % 2])

	unique = []
	for number in numbers:
		if number not in unique:
			unique.append(number)
	print("unique values:", unique)


def main():
	comparison_examples()
	print("grade:", grade_score(82))
	loop_examples()
	print("found at:", find_item(["a", "b", "c"], "b"))
	print("largest:", largest_value([17, 3, 11, 5, 1]))
	print("collatz:", collatz_sequence(6))
	logical_and_bitwise_examples()
	list_iteration_examples()


if __name__ == "__main__":
	main()
