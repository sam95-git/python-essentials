# Modules and Packages: Interview Preparation

## Core Questions

### 1. Module versus package?

A module is one Python source file. A package groups modules in a directory and exposes them through a namespace.

### 2. Why use the main guard?

`if __name__ == "__main__":` runs script-only code when the file is executed directly but not when imported.

### 3. What does an import do?

Python locates and executes a module once, caches it in `sys.modules`, and binds requested names in the importing namespace.

### 4. Why avoid wildcard imports?

They make name origins unclear and can overwrite existing names. Explicit imports are easier to read and analyze.

### 5. Why use virtual environments?

They isolate dependency versions between projects and reduce system-level conflicts.

## Output Questions

```python
# module_a.py
value = 10

# app.py
from module_a import value
value = 20
print(value)
```

**Answer:** `20`; importing binds a local name that can later be rebound.

```python
import math
print(math.ceil(2.1))
```

**Answer:** `3`.

## Common Traps

- Importing a module executes its top-level code once.
- A local file can shadow a standard-library or third-party module.
- Circular imports often indicate tangled module responsibilities.
- Changing `sys.path` at runtime is usually a design smell.
- Package-relative imports need correct package context.

## Practice

1. Split a calculator into a package with `operations.py` and `cli.py`.
2. Add a main guard and import the module without side effects.
3. Create a virtual environment and record dependencies.
4. Explain why a circular import occurs and refactor it.
