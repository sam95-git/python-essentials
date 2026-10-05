# Python Strings

Strings are **immutable sequences of Unicode code points** used to represent text. They support indexing, slicing, iteration, formatting, and many built-in methods.

## Creating Strings

Use matching single or double quotes. Triple quotes are convenient for multiline strings.

```python
single = 'Python'
double = "Python"
multiline = """first line
second line"""
```

Escape sequences represent special characters insiVde a string:

| Escape | Meaning |
| --- | --- |
| `\n` | Newline |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single quote |
| `\"` | Double quote |

```python
print("line one\nline two")
print('It\'s Python')
print("She said \"hello\"")
```

A raw string, prefixed with `r`, treats most backslashes as literal characters. Raw strings are useful for Windows paths and regular expressions, but cannot end with a single backslash.

```python
path = r"C:\Users\Ada\notes.txt"
print(path)
```

## Indexing, Slicing, and Iteration

Strings are sequences. Indexing starts at zero; negative indices count from the end. Slices include the start index and exclude the stop index.

```python
word = "Python"
print(word[0])      # P
print(word[-1])     # n
print(word[1:4])    # yth
print(word[:2])     # Py
print(word[::2])    # Pto
print(word[::-1])   # nohtyP
```

An invalid single index raises `IndexError`, while slices safely clip to the available range. Iterate character by character with `for`:

```python
for character in "cat":
    print(character)
```

## Immutability and String Operations

Strings cannot be changed in place. String methods and operations return new strings; they do not alter the original.

```python
word = "python"
uppercase = word.upper()
print(word)       # python
print(uppercase)  # PYTHON
```

- `+` concatenates strings.
- `*` repeats a string by an integer count.
- `in` checks whether a substring is present.

```python
print("Py" + "thon")       # Python
print("ha" * 3)             # hahaha
print("th" in "Python")     # True
```

For many pieces, collect the strings and use `str.join()` rather than repeatedly concatenating in a loop:

```python
parts = ["Python", "is", "readable"]
sentence = " ".join(parts)
print(sentence)
```

## Important String Methods

String methods return new values because strings are immutable.

### Case conversion

- `.lower()` and `.upper()` change letter case.
- `.casefold()` is intended for robust caseless matching, particularly with Unicode text.
- `.capitalize()` uppercases the first character and lowercases the rest.
- `.title()` applies title-style capitalization; it is not a general natural-language title formatter.

```python
text = "PyThOn"
print(text.lower())      # python
print(text.upper())      # PYTHON
print("Straße".casefold())  # strasse
```

For case-insensitive comparisons, normalize both sides with `casefold()`:

```python
left = "Straße"
right = "STRASSE"
print(left.casefold() == right.casefold())  # True
```

### Trimming whitespace or edge characters

- `.strip()` removes leading and trailing whitespace.
- `.lstrip()` and `.rstrip()` remove whitespace from one side.
- An optional argument is a **set of characters to remove**, not a literal substring.

```python
text = "  Python notes  \n"
print(text.strip())             # Python notes
print("---title---".strip("-")) # title
```

### Searching and testing

- `.find(substring)` returns the first index or `-1` if not found.
- `.index(substring)` returns the first index or raises `ValueError` if not found.
- `.count(substring)` counts non-overlapping occurrences.
- `.startswith(prefix)` and `.endswith(suffix)` return Booleans.

```python
text = "banana"
print(text.find("na"))          # 2
print(text.count("an"))         # 2
print(text.startswith("ba"))    # True
print(text.endswith("na"))      # True
```

Membership is checked with the `in` operator, not a string method: `"ana" in "banana"` evaluates to `True`.

Character classification methods include `.isalpha()`, `.isdigit()`, `.isdecimal()`, `.isnumeric()`, `.isalnum()`, and `.isspace()`. They test the entire string, and Unicode rules mean that digit-related methods have different scopes. For example, `.isdigit()` is not a complete validator for signed or decimal number text.

```python
print("Python".isalpha())  # True
print("123".isdigit())     # True
print("12.5".isdigit())    # False
print("  ".isspace())      # True
```

### Splitting and joining

- `.split()` divides on runs of whitespace when no separator is given.
- `.split(separator)` divides on the exact separator; repeated separators can produce empty fields.
- `.rsplit()` splits from the right.
- `.splitlines()` splits at line boundaries.
- `.partition(separator)` splits at the first occurrence and always returns a 3-tuple: before, separator, after. If absent, the separator and after fields are empty.
- `separator.join(iterable)` joins strings using the separator between elements.

```python
line = "red,green,blue"
print(line.split(","))                   # ['red', 'green', 'blue']
print(" a   b ".split())                 # ['a', 'b']
print(line.partition(","))               # ('red', ',', 'green,blue')
print(" / ".join(["home", "ada", "docs"]))  # home / ada / docs
```

`join()` expects an iterable of strings; convert non-string values explicitly or format them first.

### Replacing and aligning

- `.replace(old, new, count)` returns a copy with matching text replaced.
- `.removeprefix(prefix)` and `.removesuffix(suffix)` remove an exact prefix or suffix if present.
- `.center(width)`, `.ljust(width)`, and `.rjust(width)` align text in a field.

```python
message = "Python 3"
print(message.replace("3", "4"))
print("unhappy".removeprefix("un"))
print("Ada".center(7, "-"))
```

## String Formatting

Prefer **f-strings** for readable interpolation. Expressions inside braces are evaluated at runtime; format specifications control precision and alignment.

```python
name = "Ada"
score = 93.456
print(f"{name} scored {score:.1f}%")  # Ada scored 93.5%
print(f"{name:>8}")                   # right-aligned in width 8
```

`str.format()` is also used in existing code, while `%` formatting is mostly legacy:

```python
print("{} has {} books".format("Ada", 3))
```

## Unicode and Encoding

Python `str` represents Unicode text. `len(text)` counts code points, not necessarily user-perceived characters: some visible characters are made of multiple code points. For example, a letter with a combining accent may have length 2.

Text encoding converts between Unicode strings and bytes:

```python
text = "café"
data = text.encode("utf-8")
restored = data.decode("utf-8")
print(restored)
```

When reading and writing text files, specify an encoding such as `encoding="utf-8"` for consistent behavior across systems. Use `.encode()` to get bytes and `.decode()` to turn bytes into text.

## Solved String Exercises

### Reverse text

```python
def reverse_text(text):
    return text[::-1]


print(reverse_text("Python"))  # nohtyP
```

### Normalize and check a palindrome

This version ignores case, spaces, and punctuation. It compares Unicode alphanumeric characters after case folding.

```python
def is_palindrome(text):
    normalized = "".join(
        character.casefold()
        for character in text
        if character.isalnum()
    )
    return normalized == normalized[::-1]


print(is_palindrome("A man, a plan, a canal: Panama"))  # True
```

### Count character frequency

```python
from collections import Counter


def character_counts(text):
    return Counter(text)


print(character_counts("banana"))
```

Expected counts: `a` appears 3 times, `n` 2 times, and `b` once.

### Check whether two strings are anagrams

This version ignores case and non-alphanumeric characters. Sorting both normalized strings is simple; a frequency counter is preferable when avoiding a sort is important.

```python
from collections import Counter


def normalized_characters(text):
    return "".join(character.casefold() for character in text if character.isalnum())


def are_anagrams(first, second):
    return Counter(normalized_characters(first)) == Counter(normalized_characters(second))


print(are_anagrams("Dormitory", "Dirty room!!"))  # True
```

### Find the first non-repeating character

```python
from collections import Counter


def first_unique_character(text):
    counts = Counter(text)
    for character in text:
        if counts[character] == 1:
            return character
    return None


print(first_unique_character("swiss"))  # w
```

### Reverse word order

```python
def reverse_word_order(sentence):
    return " ".join(sentence.split()[::-1])


print(reverse_word_order("Python makes text processing clear"))
# clear processing text makes Python
```

## String Design and Performance Notes

- Never try to assign to a string index; build a new string instead.
- Use `"".join(parts)` when assembling many fragments.
- Choose `.find()` when absence is an ordinary case; use `.index()` when absence should raise an error.
- Use `casefold()` rather than `lower()` for Unicode-aware caseless matching.
- `strip(chars)` removes any of the supplied edge characters, not the exact substring `chars`.
- Use regular expressions only when ordinary string methods are not expressive enough.

## String Interview Questions and Practice

### Frequently asked questions

**1. Are strings mutable?**

No. They are immutable; operations such as `.replace()` return a new string.

**2. What is the difference between `find()` and `index()`?**

Both search for a substring. `find()` returns `-1` if it is absent; `index()` raises `ValueError`.

**3. What is the difference between `split()` and `partition()`?**

`split()` returns a list of parts, potentially many. `partition()` splits once and always returns a 3-tuple.

**4. What is the difference between `lower()` and `casefold()`?**

Both normalize case, but `casefold()` is more aggressive and is designed for caseless Unicode matching.

**5. Does `strip("ab")` remove the substring `"ab"`?**

No. It removes any sequence of the characters `a` and `b` from both ends until another character is reached.

**6. What does `"-".join(["a", "b"])` return?**

`"a-b"`. `join()` is called on the separator and requires string elements.

**7. Why can `len(text)` differ from the number of visible characters?**

`len()` counts Unicode code points. Some visible grapheme clusters, such as a base letter plus a combining mark, contain multiple code points.

### Output and reasoning questions

**1. What is printed?**

```python
text = "Python"
text.upper()
print(text)
```

**Answer:** `Python`; the original string is unchanged because strings are immutable.

**2. What is printed?**

```python
print("banana".find("na"), "banana".count("an"))
```

**Answer:** `2 2`.

**3. What is printed?**

```python
print("a,b,c".split(","))
print("a,b,c".partition(","))
```

**Answer:** `['a', 'b', 'c']`, then `('a', ',', 'b,c')`.

**4. What is printed?**

```python
print("  data  ".strip())
print("mississippi".strip("mi"))
```

**Answer:** First `data`, then `ssissipp`. `strip("mi")` removes any `m` or `i` character from both ends, not a matching substring.

### Common string-coding problems

1. Reverse a string without using `reversed()`.
2. Check whether a phrase is a palindrome while ignoring punctuation and case.
3. Count each character and return the most frequent one.
4. Determine whether two strings are anagrams.
5. Find the first non-repeating character; return `None` if there is none.
6. Reverse the order of words while preserving each word's spelling.
7. Compress repeated runs, for example `"aaabbc"` to `"a3b2c1"`; consider how the output should behave if compression is not shorter.
8. Find the longest common prefix in a list of strings.

These problems test iteration, dictionaries/counters, normalization, edge-case handling, and complexity—not just knowledge of string methods.