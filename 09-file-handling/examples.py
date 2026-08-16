"""Runnable examples for file and path handling."""

import json
import tempfile
from pathlib import Path


def main():
	with tempfile.TemporaryDirectory() as folder:
		path = Path(folder) / "records.json"
		payload = {"language": "Python", "topics": ["files", "paths"]}
		path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
		restored = json.loads(path.read_text(encoding="utf-8"))
		print("exists:", path.exists())
		print("language:", restored["language"])

		text_path = Path(folder) / "notes.txt"
		with text_path.open("w", encoding="utf-8") as file:
			file.write("one\ntwo\n")
		with text_path.open(encoding="utf-8") as file:
			lines = [line.strip() for line in file]
		print("lines:", lines)


if __name__ == "__main__":
	main()
