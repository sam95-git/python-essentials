"""Runnable examples for exception handling."""


class ConfigurationError(Exception):
	"""Raised when required configuration is invalid."""


def parse_integer(text):
	try:
		return int(text)
	except ValueError as error:
		raise ValueError(f"not an integer: {text!r}") from error


def safe_divide(first, second):
	try:
		return first / second
	except ZeroDivisionError:
		return None


def read_setting(settings, name):
	try:
		return settings[name]
	except KeyError as error:
		raise ConfigurationError(f"missing setting: {name}") from error


def main():
	print("parsed:", parse_integer("42"))
	print("invalid parse:")
	try:
		parse_integer("abc")
	except ValueError as error:
		print(error)

	print("divide:", safe_divide(10, 0))
	try:
		read_setting({}, "host")
	except ConfigurationError as error:
		print(error)


if __name__ == "__main__":
	main()
