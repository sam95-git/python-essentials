"""Runnable examples for classes, inheritance, properties, and dataclasses."""

from dataclasses import dataclass


class Account:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount <= 0:
			raise ValueError("deposit must be positive")
		self.balance += amount


class Animal:
	def speak(self):
		raise NotImplementedError


class Dog(Animal):
	def speak(self):
		return "woof"


@dataclass(frozen=True)
class Point:
	x: float
	y: float


def main():
	account = Account("Ada", 100)
	account.deposit(50)
	print("account:", account.owner, account.balance)
	print("polymorphism:", Dog().speak())
	print("point:", Point(3, 4))


if __name__ == "__main__":
	main()
