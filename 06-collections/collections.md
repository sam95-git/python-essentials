# Python Collections

Collections store multiple values. Choose a type based on ordering, uniqueness, mutability, and lookup needs.

## 1. Lists

Lists are ordered and mutable. They allow duplicates and mixed data types.

```python
numbers = [10, 20, 30]
numbers.append(40)
numbers[0] = 5
print(numbers[-1], numbers[1:3])
```

Useful methods include `append`, `extend`, `insert`, `remove`, `pop`, `sort`, and `reverse`. `sort()` changes the list; `sorted()` returns a new sorted list.

## 2. Tuples

Tuples are ordered and immutable. They are useful for fixed records and can be used as dictionary keys when their elements are hashable.

```python
point = (3, 4)
x, y = point
single = (42,)
```

Tuple packing and unpacking support clean swaps and multiple return values.

## 3. Sets

Sets contain unique hashable values and provide efficient membership tests. They are unordered collections.

```python
tags = {"python", "data", "python"}
tags.add("code")
print("data" in tags)
```

Set operators include union `|`, intersection `&`, difference `-`, and symmetric difference `^`.

## 4. Dictionaries

Dictionaries map unique hashable keys to values. They preserve insertion order in modern Python versions.

```python
person = {"name": "Ada", "age": 36}
person["role"] = "developer"
print(person.get("email", "not provided"))
```

Use `keys()`, `values()`, and `items()` for iteration. `get()` avoids `KeyError`; `setdefault()` can initialize a missing key.

## 5. Copying and Mutability

Assignment creates another reference to the same mutable object. Use `copy()` or slicing for a shallow copy. Use `copy.deepcopy()` for nested independent objects when needed.

```python
original = [[1], [2]]
alias = original
shallow = original.copy()
```

The inner lists remain shared in a shallow copy.

## 6. Comprehensions and Selection

```python
squares = [number * number for number in range(5)]
unique_lengths = {len(word) for word in ["Python", "code", "Python"]}
lookup = {number: number ** 2 for number in range(4)}
```

Use comprehensions for simple transformations. Use a regular loop when logic becomes nested or difficult to scan.

## 7. Choosing a Collection

| Need | Use |
| --- | --- |
| Ordered, editable sequence | `list` |
| Fixed ordered record | `tuple` |
| Unique values and set algebra | `set` |
| Key-value lookup | `dict` |
| Queue operations at both ends | `collections.deque` |

Avoid removing items from a collection while iterating over it. Build a filtered collection or iterate over a copy.
