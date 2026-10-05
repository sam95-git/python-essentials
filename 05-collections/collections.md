# Python Collections

Collections store multiple values in one object. Select a collection based on whether you need ordering, mutability, unique elements, or key-based lookup.

| Collection | Ordered | Mutable | Duplicates | Typical use |
| --- | --- | --- | --- | --- |
| `list` | Yes | Yes | Yes | Editable sequence |
| `tuple` | Yes | No* | Yes | Fixed record or grouped values |
| `set` | No | Yes | No | Unique values and set operations |
| `dict` | Insertion ordered | Yes | Keys are unique | Key-value lookup |

\* A tuple's references cannot be reassigned, but it may contain a mutable object that can itself be changed.

## Lists

A **list** is an ordered, mutable sequence written with square brackets. It can hold values of different types, including nested collections. List indices start at zero; negative indices count from the end.

```python
numbers = [10, 5, 7, 2, 1]
print(numbers[0])   # first element
print(numbers[-1])  # last element
numbers[0] = 111    # update an element
```

An index outside the list's valid range raises `IndexError`. `len(items)` returns the number of elements currently in the list.

### Add and remove elements

- `append(value)` adds one element to the end.
- `insert(index, value)` inserts before the given index; existing elements shift right.
- `extend(iterable)` adds each element from an iterable.
- `pop(index)` removes and returns an element (last element by default).
- `remove(value)` removes the first matching value and raises `ValueError` if absent.
- `del items[index]` deletes by index; `del items[start:stop]` deletes a slice; `del items` removes the name binding.

```python
items = [1, 2, 3]
items.append(4)
items.insert(1, 10)
last_item = items.pop()
del items[0]
```

### Slicing

The general form is `items[start:stop:step]`. The `start` is included and `stop` is excluded. Omitted boundaries use the start or end of the sequence; a negative step can reverse traversal.

```python
values = [10, 8, 6, 4, 2]
print(values[1:3])   # [8, 6]
print(values[:3])    # [10, 8, 6]
print(values[3:])    # [4, 2]
print(values[::-1])  # [2, 4, 6, 8, 10]
```

`items[:]` creates a **shallow copy** of the outer list. Nested objects are still shared. A normal assignment such as `alias = items` creates another reference to the same list, not a copy.

### Membership and iteration

`in` and `not in` test whether a value is present. For lists, membership compares against elements; it does not search inside strings contained in the list.

```python
colors = ["red", "blue"]
print("red" in colors)       # True
print("r" in colors)         # False
for color in colors:
	print(color)
```

Iterate over values directly when possible. Use `enumerate()` when both index and value are needed.

```python
for index, value in enumerate(colors):
	print(index, value)
```

### Sorting

- `items.sort()` sorts a list **in place** and returns `None`.
- `sorted(items)` returns a new sorted list and leaves the original unchanged.
- Sorting is stable: elements with equal sort keys retain their relative order.
- Python's built-in sorting is preferred for real code. Bubble sort is useful as a learning exercise, but has $O(n^2)$ average and worst-case time complexity.

```python
values = [8, 10, 6, 2, 4]
print(sorted(values))
values.sort(reverse=True)
print(values)
```

Bubble sort repeatedly compares neighboring elements and swaps out-of-order pairs until a full pass makes no swaps:

```python
def bubble_sort(values):
	result = values[:]
	swapped = True
	while swapped:
		swapped = False
		for index in range(len(result) - 1):
			if result[index] > result[index + 1]:
				result[index], result[index + 1] = result[index + 1], result[index]
				swapped = True
	return result


print(bubble_sort([8, 10, 6, 2, 4]))
```

### List comprehensions

A **list comprehension** creates a new list from an iterable. It can transform each item, filter items, or do both. Its general form is `[expression for item in iterable if condition]`; the `if` filter is optional.

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
odd_squares = [number ** 2 for number in numbers if number % 2 == 1]
print(squares)      # [1, 4, 9, 16, 25]
print(odd_squares)  # [1, 9, 25]
```

Use regular loops when a comprehension becomes difficult to read.

## Mutability, Aliases, and Copies

Lists are mutable objects. Assignment copies a reference, so aliases point to the same list:

```python
first = [1, 2]
alias = first
alias.append(3)
print(first)  # [1, 2, 3]
```

A **shallow copy** creates a new outer collection but keeps references to the original's nested objects. `list.copy()`, `copy.copy()`, and `items[:]` make shallow copies. A **deep copy** recursively copies nested objects too, so changes to the original structure do not affect the copy.

```python
import copy

original = [["Python"], ["SQL"]]
alias = original                 # same outer list
shallow = copy.copy(original)    # new outer list; inner lists are shared
deep = copy.deepcopy(original)   # outer and inner lists are copied

original.append(["Go"])
original[0].append("Rust")

print(alias)
print(shallow)
print(deep)
```

Output:

```text
[['Python', 'Rust'], ['SQL'], ['Go']]
[['Python', 'Rust'], ['SQL']]
[['Python'], ['SQL']]
```

The alias sees both changes because it refers to the same outer list. The shallow copy does not see the new outer element `['Go']`, but it sees the change inside the shared first inner list. The deep copy remains unchanged. Use `copy.deepcopy()` when nested mutable objects must be independent. Deep copying can be more expensive and may not be appropriate for every object. Avoid changing a list while iterating over it; iterate over a copy or build a filtered list instead.

### Nested Lists and Matrices

A nested list stores other lists as elements. A two-dimensional list can represent rows and columns; access a cell with `matrix[row][column]`. The outer index selects the row and the inner index selects the column.

```python
matrix = [[0 for _ in range(3)] for _ in range(2)]
matrix[1][2] = 7
print(matrix)  # [[0, 0, 0], [0, 0, 7]]
```

Avoid `[[0] * columns] * rows` for mutable cells: it repeats references to the same row. The nested comprehension above creates independent rows.

List comprehensions can be nested to construct a matrix:

```python
squares = [number ** 2 for number in range(5)]
matrix = [[row * column for column in range(3)] for row in range(2)]
```

### Three-dimensional data: buildings, floors, and rooms

Use a three-dimensional list when each value is addressed by three integer coordinates:

1. `rooms[building]` selects one building.
2. `rooms[building][floor]` selects a row of rooms on that floor.
3. `rooms[building][floor][room]` selects one room.

This structure represents **3 buildings × 15 floors × 20 rooms**. `False` means available; `True` means occupied. Because indices start at zero, building 2, floor 10, room 14 is addressed as `[1][9][13]`.

```python
rooms = [
	[[False for _ in range(20)] for _ in range(15)]
	for _ in range(3)
]

# Book room 14 on floor 10 of building 2.
rooms[1][9][13] = True
print("Occupied:", rooms[1][9][13])

# Count available rooms on the 15th floor of building 3.
available = 0
for is_occupied in rooms[2][14]:
	if not is_occupied:
		available += 1
print("Available rooms:", available)
```

To count occupied rooms in building 2, iterate over each floor and its rooms:

```python
occupied_count = 0
for floor in rooms[1]:
	for is_occupied in floor:
		if is_occupied:
			occupied_count += 1
print("Occupied rooms in building 2:", occupied_count)
```

Use named constants or small helper functions when raw indices such as `rooms[1][9][13]` would be difficult to interpret.

### List Section Quiz: Interview Practice

**1. What is the output?**

```python
lst = [1, 2, 3, 4, 5]
lst.insert(1, 6)
del lst[0]
lst.append(1)
print(lst)
```

**Answer:** `[6, 2, 3, 4, 5, 1]`.

**2. What is the output?**

```python
lst = [1, 2, 3, 4, 5]
lst_2 = []
add = 0
for number in lst:
	add += number
	lst_2.append(add)
print(lst_2)
```

**Answer:** `[1, 3, 6, 10, 15]`.

**3. What happens?**

```python
lst = []
del lst
print(lst)
```

**Answer:** `NameError`; `del lst` removes the name.

**4. What is the output?**

```python
lst = [1, [2, 3], 4]
print(lst[1])
print(len(lst))
```

**Answer:** `[2, 3]`, then `3`; the nested list is one element of the outer list.

**5. What is the result of sorting or reversing each list?**

```python
lst = ["D", "F", "A", "Z"]
lst.sort()
print(lst)

a = 3
b = 1
c = 2
lst = [a, c, b]
lst.sort()
print(lst)

a = "A"
b = "B"
c = "C"
d = " "
lst = [a, b, c, d]
lst.reverse()
print(lst)
```

**Answer:**

```text
['A', 'D', 'F', 'Z']
[1, 2, 3]
[' ', 'C', 'B', 'A']
```

**6. What is the output when the list names are aliases?**

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[0]
print(list_3)
```

**Answer:** `['C']`; all names refer to the same list.

**7. What is the output when one alias is deleted?**

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2
print(list_3)
```

**Answer:** `['B', 'C']`; deleting a name does not delete the shared list object.

**8. What is the output when the whole shared list is cleared by slice deletion?**

```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
del list_1[0]
del list_2[:]
print(list_3)
```

**Answer:** `[]`; deleting the full slice mutates the shared list.

**9. What is the output when slices make copies?**

```python
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]
del list_1[0]
del list_2[0]
print(list_3)
```

**Answer:** `['A', 'B', 'C']`; each slice created a separate outer list.

**10. Can all the membership quiz's expected results be produced?**

```python
my_list = [1, 2, "in", True, "ABC"]
```

**Answer:** Use `in`, `not in`, `not in`, and `in`, respectively. Membership checks for complete elements, not substrings, so `"A" not in my_list` is `True`. `False in my_list` is `False`; none of the listed elements compares equal to `False`.

## Tuples

A **tuple** is an ordered, immutable sequence, commonly written with parentheses. It supports indexing, slicing, iteration, membership, `len()`, concatenation, and repetition, much like a list. Use it for fixed groups of related values and multiple return values.

```python
point = (3, 4)
x, y = point
empty = ()
single_value = (42,)
```

The comma makes a one-element tuple; `(42)` is just an integer in parentheses. Tuple elements cannot be reassigned, but a mutable object inside a tuple can still be mutated. A tuple can be used as a dictionary key only if all its elements are hashable.

```python
record = ("Ada", ["Python"])
record[1].append("SQL")  # allowed: the nested list is mutable
# record[0] = "Grace"    # TypeError: tuple item assignment is not supported
```

### Tuple Section Quiz: Interview Practice

**1. What is the output?**

```python
my_tup = (1, 2, 3)
print(my_tup[2])
```

**Answer:** `3`.

**2. What is the output?**

```python
tup = 1, 2, 3
a, b, c = tup
print(a * b * c)
```

**Answer:** `6`.

**3. How do you count the occurrences of `2` in a tuple?**

```python
tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
duplicates = tup.count(2)
print(duplicates)
```

**Answer:** `4`.

**4. What is the output?**

```python
one = (7)
one_item_tuple = (7,)
print(type(one).__name__)
print(type(one_item_tuple).__name__)
```

**Answer:** `int`, then `tuple`. The comma creates the one-item tuple.

**5. What happens when this code runs?**

```python
point = (2, 5)
point[0] = 9
```

**Answer:** `TypeError`; tuple elements cannot be reassigned.

**6. What is the output?**

```python
record = ("Ada", ["Python"])
record[1].append("SQL")
print(record)
```

**Answer:** `('Ada', ['Python', 'SQL'])`. The tuple is immutable, but its nested list is mutable.

**7. Which of these can be dictionary keys?**

```python
(1, 2)
(1, [2])
```

**Answer:** `(1, 2)` can be a key because its elements are hashable. `(1, [2])` cannot because it contains a mutable, unhashable list.

## Sets

A **set** is a mutable collection of unique, hashable elements. Sets are useful for removing duplicates, fast membership tests, and mathematical set operations. Sets do not provide positional indexing, and their display/iteration order should not be relied on.

```python
tags = {"python", "data", "python"}
print(tags)  # contains only the unique values "python" and "data"
print("data" in tags)
```

Use `set()` to create an empty set: `{}` creates an empty dictionary. Elements must be hashable, so strings and integers can be elements, while lists and dictionaries cannot. A `frozenset` is an immutable set and can itself be used as a dictionary key if its elements are hashable.

### Set operations and methods

- `add(value)` adds one element; duplicates have no effect.
- `update(iterable)` adds every element from an iterable.
- `discard(value)` removes an element if present and does nothing otherwise.
- `remove(value)` removes an element but raises `KeyError` if it is absent.
- `pop()` removes and returns an arbitrary element; do not assume which one.
- `clear()` removes all elements.
- `|` / `.union()` gives the union; `&` / `.intersection()` gives the intersection.
- `-` / `.difference()` gives elements in the left set but not the right.
- `^` / `.symmetric_difference()` gives elements in exactly one of the sets.

```python
permissions_a = {"read", "write"}
permissions_b = {"read", "execute"}

print(permissions_a | permissions_b)  # union
print(permissions_a & permissions_b)  # shared permissions
print(permissions_a - permissions_b)  # only in permissions_a

permissions_a.add("admin")
permissions_a.discard("write")
print(permissions_a)
```

Use `discard()` when absence is normal, or `remove()` when absence should be treated as an error.

### Set comprehensions

A **set comprehension** uses braces and removes duplicate results automatically: `{expression for item in iterable if condition}`.

```python
words = ["pear", "plum", "pear", "fig"]
word_lengths = {len(word) for word in words}
long_words = {word.upper() for word in words if len(word) > 3}
print(word_lengths)  # {3, 4}
print(long_words)    # {'PEAR', 'PLUM'} (display order may vary)
```

### Set Section Quiz: Interview Practice

**1. What are the values and types?**

```python
values = {1, 2, 2, 3}
empty_set = set()
empty_dict = {}
print(len(values), type(empty_set).__name__, type(empty_dict).__name__)
```

**Answer:** `3 set dict`; sets discard duplicates, and `{}` creates a dictionary.

**2. What do the set operations return?**

```python
a = {1, 2, 3}
b = {3, 4}
print(a | b)
print(a & b)
print(a - b)
```

**Answer:** The union is `{1, 2, 3, 4}`, the intersection is `{3}`, and the difference is `{1, 2}`. Set display order is not guaranteed.

**3. What is the difference between `discard()` and `remove()` for a missing element?**

**Answer:** `discard(value)` does nothing; `remove(value)` raises `KeyError`.

**4. What happens here?**

```python
values = {[1, 2]}
```

**Answer:** `TypeError`; a list is mutable and unhashable, so it cannot be a set element.

**5. What values are in the comprehension result?**

```python
squares = {number ** 2 for number in [1, 2, 2, 3]}
```

**Answer:** The set contains `{1, 4, 9}`; repeated results are stored once.

## Dictionaries

A **dictionary** is a mutable mapping of unique, hashable keys to values. It preserves insertion order in supported modern Python versions. Keys are unique; assigning an existing key replaces its value. Values may be repeated and may have any type.

```python
person = {"name": "Ada", "role": "developer"}
person["role"] = "engineer"  # update an existing key
person["language"] = "Python"  # add a new key
```

Use square brackets when the key must exist; a missing key raises `KeyError`. Use `.get(key, default)` for safe lookup. Membership tests check **keys**, not values.

```python
print(person["name"])
print(person.get("location", "unknown"))
print("role" in person)  # True: checks keys
```

Common dictionary methods:

- `.keys()`, `.values()`, and `.items()` return **iterable views** of the dictionary. The views reflect later changes to the dictionary.
- `.items()` yields `(key, value)` pairs, so a loop can unpack each pair into two variables.
- `.update(other)` adds entries from another mapping or iterable of pairs; if a key already exists, its value is replaced.
- `.pop(key)` removes the requested key and returns its value. A missing key raises `KeyError` unless a default is supplied.
- `.popitem()` removes and returns the most recently inserted `(key, value)` pair.
- `.clear()` removes every entry from the dictionary.
- `.copy()` creates a **shallow copy**: the new dictionary is independent, but nested mutable values are still shared.

```python
person = {"name": "Ada", "role": "developer"}

print(list(person.keys()))
print(list(person.values()))
print(list(person.items()))

for key, value in person.items():
    print(key, "->", value)

person.update({"role": "engineer", "language": "Python"})
print(person)

removed_role = person.pop("role")
print("removed:", removed_role)

last_pair = person.popitem()
print("popped pair:", last_pair)

person_copy = person.copy()
person.clear()
print("original after clear:", person)
print("copy remains:", person_copy)
```

### Dictionary comprehensions

A **dictionary comprehension** uses braces with a key-value expression: `{key_expression: value_expression for item in iterable if condition}`.

```python
squares_by_number = {number: number ** 2 for number in range(1, 5)}
even_squares = {number: number ** 2 for number in range(1, 6) if number % 2 == 0}
print(squares_by_number)  # {1: 1, 2: 4, 3: 9, 4: 16}
print(even_squares)       # {2: 4, 4: 16}
```

If a comprehension produces duplicate keys, the later value replaces the earlier value for that key.

### Dictionary Section Quiz: Interview Practice

**1. How do you merge two dictionaries into a new dictionary?**

```python
d1 = {"Adam Smith": "A", "Judy Paxton": "B+"}
d2 = {"Mary Louis": "A", "Patrick White": "C"}
d3 = {}

for dictionary in (d1, d2):
	d3.update(dictionary)

print(d3)
```

**Answer:** `{'Adam Smith': 'A', 'Judy Paxton': 'B+', 'Mary Louis': 'A', 'Patrick White': 'C'}`.

**2. How do you convert a list to a tuple?**

```python
my_list = ["car", "Ford", "flower", "Tulip"]
t = tuple(my_list)
print(t)
```

**Answer:** `('car', 'Ford', 'flower', 'Tulip')`.

**3. How do you convert key-value pairs into a dictionary?**

```python
colors = (("green", "#008000"), ("blue", "#0000FF"))
colors_dictionary = dict(colors)
print(colors_dictionary)
```

**Answer:** `{'green': '#008000', 'blue': '#0000FF'}`.

**4. What is the output?**

```python
my_dictionary = {"A": 1, "B": 2}
copy_my_dictionary = my_dictionary.copy()
my_dictionary.clear()
print(copy_my_dictionary)
```

**Answer:** `{'A': 1, 'B': 2}`; `.copy()` creates a separate shallow dictionary.

**5. What does this loop print?**

```python
colors = {
	"white": (255, 255, 255),
	"grey": (128, 128, 128),
	"red": (255, 0, 0),
	"green": (0, 128, 0),
}

for color, rgb in colors.items():
	print(color, ":", rgb)
```

**Answer:** Four `color : rgb` lines, in insertion order: white, grey, red, then green.

## Comprehension Quick Reference

| Type | Syntax shape | Example result |
| --- | --- | --- |
| List | `[expression for item in iterable if condition]` | `[1, 4, 9]` |
| Set | `{expression for item in iterable if condition}` | `{1, 4, 9}`; duplicates removed |
| Dictionary | `{key: value for item in iterable if condition}` | `{1: 1, 2: 4}` |
| Tuple | No tuple-comprehension syntax; use a generator expression with `tuple()` | `tuple(x * x for x in range(3))` gives `(0, 1, 4)` |

```python
numbers = [1, 2, 2, 3]
as_list = [number * 2 for number in numbers]
as_set = {number * 2 for number in numbers}
as_dict = {number: number * 2 for number in numbers}
as_tuple = tuple(number * 2 for number in numbers)
```

## Choosing a Collection

- Choose a **list** for an ordered sequence that changes.
- Choose a **tuple** for an ordered record that should not be reassigned.
- Choose a **set** for unique values and efficient membership checks.
- Choose a **dictionary** for looking up values by meaningful keys.
- Use `collections.deque` for efficient append/pop operations at both ends of a queue.

## Solved Exercises

### Replace the middle, remove the last, and report length

```python
hat_list = [1, 2, 3, 4, 5]
hat_list[2] = int(input("Enter a replacement integer: "))
del hat_list[-1]
print(len(hat_list))
print(hat_list)
```

### Build the Beatles list

```python
beatles = []
beatles.extend(["John Lennon", "Paul McCartney", "George Harrison"])

for _ in range(2):
	beatles.append(input("Enter a band member: "))

del beatles[4]
del beatles[3]
beatles.insert(0, "Ringo Starr")
print(beatles)
```

### Remove duplicate numbers while preserving order

```python
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
unique_values = []

for value in my_list:
	if value not in unique_values:
		unique_values.append(value)

print("The list with unique elements only:")
print(unique_values)
```

### Store students' scores and calculate averages

```python
scores_by_student = {}

scores_by_student.setdefault("Bob", []).extend([7, 2, 9])
scores_by_student.setdefault("Andy", []).extend([3, 10, 3])

for name, scores in sorted(scores_by_student.items()):
	print(name, ":", sum(scores) / len(scores))
```

