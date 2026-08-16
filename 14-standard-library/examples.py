"""Runnable examples for selected standard-library modules."""

import math
import statistics
from collections import Counter, deque
from datetime import date, timedelta
from itertools import islice
from pathlib import Path


def main():
	values = [2, 4, 4, 8]
	print("mean:", statistics.mean(values))
	print("root:", math.sqrt(16))
	print("counts:", Counter("banana").most_common())

	queue = deque(["first", "second"])
	queue.append("third")
	print("queue item:", queue.popleft())

	print("tomorrow:", date.today() + timedelta(days=1))
	print("slice:", list(islice(range(10), 2, 6)))
	print("path:", Path("data") / "records.txt")


if __name__ == "__main__":
	main()
