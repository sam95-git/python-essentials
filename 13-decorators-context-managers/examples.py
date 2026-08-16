"""Runnable examples for decorators and context managers."""

from contextlib import contextmanager
from functools import wraps


def announce(function):
	@wraps(function)
	def wrapper(*args, **kwargs):
		print("calling", function.__name__)
		return function(*args, **kwargs)

	return wrapper


@announce
def add(first, second):
	return first + second


@contextmanager
def managed_message():
	print("enter")
	try:
		yield
	finally:
		print("exit")


def main():
	print("result:", add(2, 3))
	with managed_message():
		print("body")


if __name__ == "__main__":
	main()
