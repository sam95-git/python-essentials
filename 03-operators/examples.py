"""Runnable examples for Python operators and user interaction."""


def arithmetic_examples():
	left, right = 7, 2
	print("+", left + right)
	print("-", left - right)
	print("*", left * right)
	print("/", left / right)
	print("//", left // right)
	print("%", left % right)
	print("**", left ** right)
	print("negative floor division:", -7 // 2)


def comparison_and_logic_examples():
	age = 20
	has_ticket = True
	print("adult:", age >= 18)
	print("allowed:", age >= 18 and has_ticket)
	print("fallback:", "" or "Guest")
	print("membership:", "py" in "python")


def assignment_examples():
	score = 10
	score += 5
	score *= 2
	score //= 3
	print("updated score:", score)


def expression_examples():
	print("precedence:", 2 + 3 * 4)
	print("parentheses:", (2 + 3) * 4)
	print("power associativity:", 2 ** 3 ** 2)
	minutes = 135
	hours, remaining = divmod(minutes, 60)
	print("duration:", hours, "hours", remaining, "minutes")


def calculate_from_text(first_text, operator, second_text):
	"""Convert text input and calculate a basic arithmetic result."""
	first = float(first_text)
	second = float(second_text)
	operations = {
		"+": lambda: first + second,
		"-": lambda: first - second,
		"*": lambda: first * second,
		"/": lambda: first / second,
	}
	if operator not in operations:
		raise ValueError("Unsupported operator")
	return operations[operator]()


def interactive_calculator():
	"""Optional practice function; call it to collect values from a user."""
	try:
		first = input("First number: ")
		operator = input("Operator (+, -, *, /): ")
		second = input("Second number: ")
		print("Result:", calculate_from_text(first, operator, second))
	except ValueError as error:
		print("Input error:", error)
	except ZeroDivisionError:
		print("Input error: cannot divide by zero")


def main():
	arithmetic_examples()
	comparison_and_logic_examples()
	assignment_examples()
	expression_examples()
	print("calculator sample:", calculate_from_text("12", "+", "3"))


if __name__ == "__main__":
	main()
