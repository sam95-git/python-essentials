# Python Modules and Packages

A module is a `.py` file containing definitions. A package is a directory that groups related modules under a common namespace.

## 1. Importing

```python
import math
from pathlib import Path
import statistics as stats
```

Use `module.name` to access imported members. Import aliases can improve readability, but avoid wildcard imports because they hide where names come from.

## 2. Module Execution and `__name__`

Module-level code runs when the module is imported. Use a main guard for executable behavior:

```python
def main():
	print("run as a script")

if __name__ == "__main__":
	main()
```

This lets the file be imported without immediately running its command-line behavior.

## 3. Packages

A package organizes modules:

```text
app/
	__init__.py
	models.py
	services.py
```

Modern namespace packages may omit `__init__.py`, but an initializer remains useful for package-level setup and explicit exports.

## 4. Namespaces and Search Path

Each module has its own namespace. Imports bind names in the importing module; they do not copy source text. Python searches locations in `sys.path`, including the current project and installed packages.

Avoid naming files after standard-library modules, such as `json.py` or `random.py`, because local files can shadow the intended import.

## 5. Environments and Dependencies

Use a virtual environment to isolate project dependencies:

```text
python -m venv .venv
```

Record third-party dependencies in `requirements.txt` or project metadata. Prefer absolute imports inside packages and keep import side effects minimal.

## 6. Useful Metadata

`__file__` identifies a module's source path. `dir(module)` lists accessible names. `help(module)` provides documentation. `importlib` supports dynamic imports when a plugin architecture requires them.
