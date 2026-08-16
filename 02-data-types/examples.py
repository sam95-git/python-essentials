"""Runnable examples for Python data types and variables."""


def show_basics():
	print("Hello, Python!")
	print("Python", "data types", sep=" | ")
	print("Line one\nLine two")


def show_literals_and_types():
	values = [42, 3.14, 0b1010, "Python", True, None]
	for value in values:
		print(repr(value), "->", type(value).__name__)

	print("0xFF =", 0xFF)
	print("1_000_000 =", 1_000_000)
	print("2 ** 3 =", 2 ** 3)


def show_strings():
	word = "Python"
	print(word[0], word[-1])
	print(word[1:4])
	print("ha" * 3)
	print('She said "hello".')
	print("I'm learning Python.")


def show_variables_and_conversion():
	apples, oranges = 3, 5
	apples, oranges = oranges, apples
	total = apples + oranges
	print("apples:", apples, "oranges:", oranges, "total:", total)

	text_number = "42"
	number = int(text_number)
	print(number, type(number).__name__)
	print(float("3.5"), str(number) + " items")
	print(bool(0), bool("Python"), bool([]), bool([1]))


def main():
	show_basics()
	show_literals_and_types()
	show_strings()
	show_variables_and_conversion()


if __name__ == "__main__":
	main()
