"""Runnable examples for unittest and simple debugging-friendly code."""

import unittest


def is_leap_year(year):
	return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def divide(first, second):
	return first / second


class TestCalendar(unittest.TestCase):
	def test_divisible_by_400(self):
		self.assertTrue(is_leap_year(2000))

	def test_century_not_divisible_by_400(self):
		self.assertFalse(is_leap_year(1900))

	def test_regular_leap_year(self):
		self.assertTrue(is_leap_year(2024))

	def test_division_by_zero(self):
		with self.assertRaises(ZeroDivisionError):
			divide(1, 0)


if __name__ == "__main__":
	unittest.main()
