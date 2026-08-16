"""Runnable examples for Python string operations."""


def normalize_words(text):
	return text.strip().casefold().split()


def is_palindrome(text):
	normalized = "".join(character.casefold() for character in text if character.isalnum())
	return normalized == normalized[::-1]


def main():
	text = "  Python, code  "
	clean = text.strip().replace(",", "")
	print("clean:", clean)
	print("slice:", "Python"[1:4])
	print("words:", normalize_words(" Learn   Python "))
	print("joined:", "-".join(["readable", "and", "clear"]))
	print(f"score: {95 / 10:.1f}")
	print("palindrome:", is_palindrome("A man, a plan, a canal: Panama"))


if __name__ == "__main__":
	main()
