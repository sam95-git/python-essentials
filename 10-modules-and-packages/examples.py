"""Runnable examples for standard modules and import guards."""

import math
import statistics
from pathlib import Path


def summarize(values):
	return {
		"mean": statistics.mean(values),
		"maximum": max(values),
		"root_of_maximum": math.sqrt(max(values)),
	}


def main():
	print("summary:", summarize([4, 9, 16]))
	print("current file name:", Path(__file__).name)


if __name__ == "__main__":
	main()
