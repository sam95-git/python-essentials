"""Runnable examples for lists, tuples, sets, and dictionaries."""


def main():
	numbers = [3, 1, 2]
	numbers.append(4)
	print("list:", sorted(numbers))

	point = (3, 4)
	x, y = point
	print("tuple:", x, y)

	tags = {"python", "code", "python"}
	tags |= {"learning"}
	print("set:", sorted(tags))

	scores = {"Ada": 95, "Grace": 88}
	scores["Linus"] = 91
	print("dictionary:", sorted(scores.items()))
	print("missing:", scores.get("Unknown", 0))

	print("squares:", [number ** 2 for number in range(5)])
	frequencies = {}
	for letter in "banana":
		frequencies[letter] = frequencies.get(letter, 0) + 1
	print("frequencies:", frequencies)

	original = [[1], [2]]
	shallow = original.copy()
	original[0].append(9)
	print("shallow copy:", shallow)


if __name__ == "__main__":
	main()
