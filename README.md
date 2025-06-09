# Python-Practice

Learning Python with CodeWithHarry

## Python Practice Projects 🐍

This repository contains Python practice projects I'm working on while learning from [CodeWithHarry](https://www.codewithharry.com/). These help me understand core Python concepts.

## Topics Covered

- Variables and Data Types
- Conditionals and Loops
- Functions
- And more...

## How to Run

```bash
python main.py
```

## Note on Python's Typing

Python is a dynamically typed language, meaning you don't need to declare variable types explicitly. The type of a variable is determined at runtime, unlike statically typed languages where types are checked at compile time.

## Variable Naming Rules in Python

- Variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
- They must begin with a letter or underscore, not a digit.
- Variable names are case-sensitive (`myVar` and `myvar` are different).
- Reserved keywords (like `for`, `if`, `class`, etc.) cannot be used as variable names.
- Avoid using special characters (such as `@`, `$`, `%`, etc.) in variable names.
- Use descriptive names to make code more readable.

**Examples:**

```python
valid_name = 10
_validName = 20
valid_name_2 = 30
# Invalid examples:
# 2invalid = 40
# my-var = 50
# for = 60
```

## Basic Rules of Python

- Indentation is crucial; it defines code blocks (typically 4 spaces).
- Statements end with a newline, not a semicolon.
- Variable names are case-sensitive and should be descriptive.
- Comments start with `#` for single-line or triple quotes for multi-line.
- Strings can be enclosed in single (`'`), double (`"`), or triple quotes (`'''` or `"""`).
- Python uses dynamic typing; variable types can change at runtime.
- Use `import` to include modules and libraries.
- Functions are defined using the `def` keyword.
- Code should follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines for readability.

## Built-in Data Types in Python

Python supports several built-in data types, including:

- **Numbers:** `int`, `float`, `complex`
- **Strings:** `str`
- **Boolean:** `bool`
- **Sequences:** `list`, `tuple`, `range`
- **Lists:** Ordered, mutable collections (`list`)
  - Elements maintain insertion order.
  - Items can be changed, added, or removed.
  - Defined with square brackets: `[1, 2, 3]`.
- **Tuples:** Ordered, immutable collections (`tuple`)
  - Elements maintain insertion order.
  - Items cannot be changed after creation.
  - Defined with parentheses: `(1, 2, 3)`.
- **Mapping:** `dict`
  - Stores key-value pairs.
  - Keys must be unique and immutable.
  - Values can be of any type and are mutable.
  - Defined with curly braces: `{"key": "value"}`.
- **Set Types:** `set`, `frozenset`
- **None Type:** `NoneType`

**Examples:**

```python
num = 42                # int
pi = 3.14               # float
name = "Harry"          # str
is_active = True        # bool
numbers = [1, 2, 3]     # list
coordinates = (4, 5)    # tuple
user = {"id": 1}        # dict
unique = {1, 2, 3}      # set
nothing = None          # NoneType
```

## Typecasting in Python

Typecasting is the process of converting a variable from one data type to another. Python provides built-in functions for typecasting:

- `int()`: Converts to integer
- `float()`: Converts to floating-point number
- `str()`: Converts to string
- `bool()`: Converts to boolean
- `list()`, `tuple()`, `set()`, `dict()`: Convert to respective collection types

**Examples:**

```python
a = "123"
b = int(a)      # b is now 123 (int)
c = float(a)    # c is now 123.0 (float)
d = str(456)    # d is now "456" (str)
e = bool(0)     # e is False
f = list("abc") # f is ['a', 'b', 'c']
```

### Example: Taking Input and Typecasting

When you use the `input()` function in Python, the value you get is always of type `str` (string), even if the user enters a number. You need to typecast it to the desired type before using it in calculations.

```python
user_input = input("Enter a number: ")  # input is always a string
print(type(user_input))                 # <class 'str'>

# Convert input to integer
number = int(user_input)
print(number + 10)                      # Now you can perform arithmetic
```

> **Important Note:**  
> Always validate user input before typecasting to avoid runtime errors. For example, converting a non-numeric string to `int` will raise a `ValueError`. Use `try`/`except` blocks to handle such cases gracefully.

**Example with input validation:**

```python
user_input = input("Enter a number: ")
try:
        number = int(user_input)
        print("You entered:", number)
except ValueError:
        print("Invalid input! Please enter a valid number.")
```

## Operators in Python

Operators are special symbols or keywords that perform operations on operands (variables and values). Python supports several types of operators:

### 1. Arithmetic Operators

Used for mathematical operations:

| Operator | Description        | Example         |
|----------|-------------------|-----------------|
| `+`      | Addition          | `a + b`         |
| `-`      | Subtraction       | `a - b`         |
| `*`      | Multiplication    | `a * b`         |
| `/`      | Division          | `a / b`         |
| `//`     | Floor Division    | `a // b`        |
| `%`      | Modulus           | `a % b`         |
| `**`     | Exponentiation    | `a ** b`        |

**Example:**

```python
x = 10
y = 3
print(x + y)   # 13
print(x / y)   # 3.333...
print(x // y)  # 3
print(x % y)   # 1
print(x ** y)  # 1000
```

### 2. Assignment Operators

Used to assign values to variables:

| Operator | Example   | Equivalent to   |
|----------|-----------|----------------|
| `=`      | `a = 5`   |                |
| `+=`     | `a += 2`  | `a = a + 2`    |
| `-=`     | `a -= 2`  | `a = a - 2`    |
| `*=`     | `a *= 2`  | `a = a * 2`    |
| `/=`     | `a /= 2`  | `a = a / 2`    |
| `//=`    | `a //= 2` | `a = a // 2`   |
| `%=`     | `a %= 2`  | `a = a % 2`    |
| `**=`    | `a **= 2` | `a = a ** 2`   |

### 3. Comparison Operators

Used to compare values; result is `True` or `False`:

| Operator | Description         | Example      |
|----------|--------------------|--------------|
| `==`     | Equal to           | `a == b`     |
| `!=`     | Not equal to       | `a != b`     |
| `>`      | Greater than       | `a > b`      |
| `<`      | Less than          | `a < b`      |
| `>=`     | Greater or equal   | `a >= b`     |
| `<=`     | Less or equal      | `a <= b`     |

### 4. Logical Operators

Used to combine conditional statements:

| Operator | Description | Example           |
|----------|-------------|-------------------|
| `and`    | Logical AND | `a > 2 and b < 5` |
| `or`     | Logical OR  | `a > 2 or b < 5`  |
| `not`    | Logical NOT | `not(a > 2)`      |

### 5. Membership Operators

Test if a value is in a sequence:

| Operator | Description      | Example         |
|----------|-----------------|-----------------|
| `in`     | Value present   | `'a' in 'cat'`  |
| `not in` | Value not present | `'x' not in 'cat'` |

### 6. Identity Operators

Compare memory locations of two objects:

| Operator | Description      | Example     |
|----------|-----------------|-------------|
| `is`     | Same object     | `a is b`    |
| `is not` | Not same object | `a is not b`|

### 7. Bitwise Operators

Operate on binary representations:

| Operator | Description      | Example    |
|----------|-----------------|------------|
| `&`      | AND             | `a & b`    |
| `|`      | OR              | `a | b`    |
| `^`      | XOR             | `a ^ b`    |
| `~`      | NOT             | `~a`       |
| `<<`     | Left Shift      | `a << 2`   |
| `>>`     | Right Shift     | `a >> 2`   |

**Example:**

```python
a = 5      # 0b0101
b = 3      # 0b0011
print(a & b)  # 1 (0b0001)
print(a | b)  # 7 (0b0111)
```

> **Tip:** Use parentheses to clarify complex expressions and control operator precedence.


## String Methods and Functions in Python

Strings in Python are sequences of characters and come with many built-in methods for manipulation and analysis. Here are some commonly used string methods and functions:

### Common String Methods

| Method            | Description                                      | Example                        |
|-------------------|--------------------------------------------------|--------------------------------|
| `str.upper()`     | Converts all characters to uppercase              | `"hello".upper()` → `"HELLO"`  |
| `str.lower()`     | Converts all characters to lowercase              | `"Hello".lower()` → `"hello"`  |
| `str.title()`     | Capitalizes the first letter of each word         | `"hello world".title()` → `"Hello World"` |
| `str.capitalize()`| Capitalizes the first character                   | `"python".capitalize()` → `"Python"` |
| `str.strip()`     | Removes leading/trailing whitespace               | `"  hi  ".strip()` → `"hi"`    |
| `str.lstrip()`    | Removes leading whitespace                        | `"  hi".lstrip()` → `"hi"`     |
| `str.rstrip()`    | Removes trailing whitespace                       | `"hi  ".rstrip()` → `"hi"`     |
| `str.replace(a, b)`| Replaces substring `a` with `b`                  | `"cat".replace("c", "b")` → `"bat"` |
| `str.find(sub)`   | Returns lowest index of substring, or `-1` if not found | `"hello".find("e")` → `1` |
| `str.count(sub)`  | Counts occurrences of substring                   | `"banana".count("a")` → `3`    |
| `str.split(sep)`  | Splits string into a list by separator            | `"a,b,c".split(",")` → `['a','b','c']` |
| `str.join(list)`  | Joins elements of a list into a string            | `",".join(['a','b','c'])` → `"a,b,c"` |
| `str.startswith(prefix)` | Checks if string starts with prefix         | `"hello".startswith("he")` → `True` |
| `str.endswith(suffix)`   | Checks if string ends with suffix           | `"hello".endswith("lo")` → `True` |

### String Functions

- `len(s)`: Returns the length of the string.
- `str()`: Converts an object to a string.
- `ord(c)`: Returns the Unicode code point of character `c`.
- `chr(i)`: Returns the character for Unicode code point `i`.

### Examples

```python
s = "  Hello, Python!  "
print(s.strip())            # "Hello, Python!"
print(s.lower())            # "  hello, python!  "
print(s.replace("Python", "World"))  # "  Hello, World!  "
print(len(s))               # 17

words = "apple,banana,cherry"
fruits = words.split(",")   # ['apple', 'banana', 'cherry']
joined = "-".join(fruits)   # "apple-banana-cherry"
```

> **Tip:** Strings are immutable in Python, so string methods return new strings and do not modify the original.

For more, see the [official Python string methods documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

## String Formatting: f-Strings and `format()`

Python provides several ways to format strings, with f-strings (formatted string literals) and the `str.format()` method being the most common and modern approaches.

### f-Strings (Python 3.6+)

f-Strings allow you to embed expressions inside string literals, using curly braces `{}`. Prefix the string with `f` or `F`.

**Example:**

```python
name = "Harry"
age = 25
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Harry and I am 25 years old.
```

You can also use expressions inside the curly braces:

```python
a = 5
b = 10
print(f"Sum: {a + b}")
# Output: Sum: 15
```

### `str.format()` Method

The `format()` method inserts values into placeholders `{}` in a string.

**Example:**

```python
name = "Harry"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
# Output: My name is Harry and I am 25 years old.
```

You can use positional or named arguments:

```python
print("Name: {n}, Age: {a}".format(n=name, a=age))
```

### Formatting Numbers

You can format numbers (e.g., decimals, padding) with both f-strings and `format()`:

```python
pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")           # f-string
print("Pi rounded to 2 decimals: {:.2f}".format(pi))   # format()
```

> **Tip:** f-Strings are recommended for new code due to their readability and performance.

For more details, see the [official Python f-strings documentation](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

## Functions and Arguments in Python

Functions are reusable blocks of code that perform a specific task. You define a function using the `def` keyword, followed by the function name and parentheses containing parameters.

### Defining a Function

```python
def greet(name):
  print(f"Hello, {name}!")
```

### Calling a Function

```python
greet("Harry")  # Output: Hello, Harry!
```

---

## Function Arguments

Python functions can accept different types of arguments:

### 1. Positional Arguments

Arguments passed to a function in the correct positional order.

```python
def add(a, b):
  return a + b

result = add(2, 3)  # a=2, b=3
```

### 2. Keyword Arguments

Arguments passed by explicitly specifying the parameter name, regardless of their position.

```python
def introduce(name, age):
  print(f"{name} is {age} years old.")

introduce(age=25, name="Harry")  # Order doesn't matter
```

### 3. Default Arguments

You can assign default values to parameters. If the argument is not provided, the default is used.

```python
def greet(name, message="Hello"):
  print(f"{message}, {name}!")

greet("Harry")                # Output: Hello, Harry!
greet("Harry", message="Hi")  # Output: Hi, Harry!
```

### 4. Mixing Arguments

Positional arguments must come before keyword arguments.

```python
def power(base, exponent=2):
  return base ** exponent

print(power(3))         # 9 (exponent defaults to 2)
print(power(3, 3))      # 27
print(power(base=2, exponent=5))  # 32
```

> **Tip:** Use keyword arguments for clarity, especially when a function has many parameters or default values.

For more, see the [official Python functions documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions).

## Lambda Functions in Python

A **lambda function** is a small, anonymous function defined with the `lambda` keyword. Lambda functions can have any number of arguments but only one expression. They are often used for short, simple operations where defining a full function is unnecessary.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```

### Usage

Lambda functions are commonly used with functions like `map()`, `filter()`, and `sorted()`:

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
```

### Key Points

- Lambda functions are limited to a single expression.
- They return the value of the expression automatically.
- Useful for short, throwaway functions.

> **Tip:** Use lambda functions for simple operations; for complex logic, use a regular `def` function.

For more, see the [official Python lambda documentation](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions).

## List Methods in Python

Lists are mutable, ordered collections in Python with many built-in methods for adding, removing, and manipulating elements.

### Common List Methods

| Method              | Description                                         | Example                                 |
|---------------------|-----------------------------------------------------|-----------------------------------------|
| `append(x)`         | Adds item `x` to the end of the list                | `lst.append(4)`                         |
| `extend(iterable)`  | Adds all items from an iterable to the end          | `lst.extend([5, 6])`                    |
| `insert(i, x)`      | Inserts item `x` at position `i`                    | `lst.insert(1, 10)`                     |
| `remove(x)`         | Removes first occurrence of `x`                     | `lst.remove(2)`                         |
| `pop([i])`          | Removes and returns item at index `i` (default last)| `lst.pop()`                             |
| `clear()`           | Removes all items from the list                     | `lst.clear()`                           |
| `index(x)`          | Returns index of first occurrence of `x`            | `lst.index(3)`                          |
| `count(x)`          | Returns number of occurrences of `x`                | `lst.count(2)`                          |
| `sort()`            | Sorts the list in place                             | `lst.sort()`                            |
| `reverse()`         | Reverses the list in place                          | `lst.reverse()`                         |
| `copy()`            | Returns a shallow copy of the list                  | `lst2 = lst.copy()`                     |

**Example:**

```python
lst = [1, 2, 3]
lst.append(4)           # [1, 2, 3, 4]
lst.extend([5, 6])      # [1, 2, 3, 4, 5, 6]
lst.insert(0, 0)        # [0, 1, 2, 3, 4, 5, 6]
lst.remove(3)           # [0, 1, 2, 4, 5, 6]
item = lst.pop()        # item=6, lst=[0, 1, 2, 4, 5]
lst.sort()              # [0, 1, 2, 4, 5]
lst.reverse()           # [5, 4, 2, 1, 0]
```

For more, see the [official Python list methods documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).

---

## List Comprehension

**List comprehension** provides a concise way to create lists using a single line of code, often replacing loops for generating new lists.

### Syntax

```python
[expression for item in iterable if condition]
```

- `expression`: The value to put in the new list.
- `item`: The variable representing each element in the iterable.
- `condition` (optional): Only include items where this is `True`.

### Examples

**Basic list comprehension:**

```python
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

**With condition:**

```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

**Nested list comprehension:**

```python
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # [(1, 3), (1, 4), (2, 3), (2, 4)]
```

> **Tip:** List comprehensions are more readable and efficient for simple list transformations.

For more, see the [official Python list comprehensions documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions).

## Tuples in Python

A **tuple** is an ordered, immutable collection of items. Once created, the elements of a tuple cannot be changed, added, or removed. Tuples are useful for grouping related data and for situations where immutability is desired.

### Creating Tuples

- Use parentheses `()` or simply separate values with commas.
- For a single-element tuple, include a trailing comma.

```python
t1 = (1, 2, 3)
t2 = 4, 5, 6
t3 = (7,)        # Single-element tuple
empty = ()       # Empty tuple
```

### Accessing Tuple Elements

- Use indexing and slicing, similar to lists.

```python
t = (10, 20, 30, 40)
print(t[1])      # 20
print(t[:2])     # (10, 20)
```

### Tuple Methods

Tuples have only two built-in methods:

| Method        | Description                                 | Example                |
|---------------|---------------------------------------------|------------------------|
| `count(x)`    | Returns the number of times `x` appears     | `t.count(10)`          |
| `index(x)`    | Returns the index of the first occurrence   | `t.index(30)`          |

### Tuple Packing and Unpacking

- **Packing:** Assigning multiple values to a tuple.
- **Unpacking:** Assigning tuple elements to variables.

```python
point = (3, 4)
x, y = point
print(x)    # 3
print(y)    # 4
```

### Immutability

- Tuples cannot be changed after creation.
- However, if a tuple contains mutable objects (like lists), those objects can be changed.

```python
t = (1, [2, 3])
t[1][0] = 99
print(t)    # (1, [99, 3])
```

### When to Use Tuples

- When you need an immutable sequence of items.
- As keys in dictionaries (if all elements are immutable).
- For returning multiple values from a function.

> **Tip:** Use tuples for fixed collections of items and lists for mutable sequences.

For more, see the [official Python tuple documentation](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences).


## Sets in Python

A **set** is an unordered collection of unique, immutable elements. Sets are useful for membership testing, removing duplicates, and performing mathematical set operations like union, intersection, and difference.

### Creating Sets

- Use curly braces `{}` or the `set()` constructor.
- Duplicates are automatically removed.

```python
s1 = {1, 2, 3}
s2 = set([2, 3, 4])
empty_set = set()  # Note: {} creates an empty dict, not a set
```

### Common Set Methods

| Method            | Description                                         | Example                      |
|-------------------|-----------------------------------------------------|------------------------------|
| `add(x)`          | Adds element `x` to the set                         | `s.add(5)`                   |
| `update(iterable)`| Adds all elements from an iterable                  | `s.update([6, 7])`           |
| `remove(x)`       | Removes `x`; raises `KeyError` if not found         | `s.remove(2)`                |
| `discard(x)`      | Removes `x` if present; does nothing if not         | `s.discard(3)`               |
| `pop()`           | Removes and returns an arbitrary element            | `item = s.pop()`             |
| `clear()`         | Removes all elements from the set                   | `s.clear()`                  |
| `copy()`          | Returns a shallow copy of the set                   | `s2 = s.copy()`              |

### Set Operations

Python sets support standard mathematical set operations, either as methods or operators:

| Operation         | Method                | Operator | Example                |
|-------------------|----------------------|----------|------------------------|
| Union             | `set1.union(set2)`    | `|`      | `s1 | s2`              |
| Intersection      | `set1.intersection(s)`| `&`      | `s1 & s2`              |
| Difference        | `set1.difference(s)`  | `-`      | `s1 - s2`              |
| Symmetric Diff.   | `set1.symmetric_difference(s)` | `^` | `s1 ^ s2`         |
| Subset            | `set1.issubset(s)`    | `<=`     | `s1 <= s2`             |
| Superset          | `set1.issuperset(s)`  | `>=`     | `s1 >= s2`             |
| Disjoint          | `set1.isdisjoint(s)`  |          | `s1.isdisjoint(s2)`    |

### Examples

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)   # Union: {1, 2, 3, 4, 5}
print(a & b)   # Intersection: {3}
print(a - b)   # Difference: {1, 2}
print(a ^ b)   # Symmetric Difference: {1, 2, 4, 5}

a.add(6)       # {1, 2, 3, 6}
a.discard(2)   # {1, 3, 6}
```

> **Tip:** Sets are unordered and do not support indexing or slicing.

For more, see the [official Python set documentation](https://docs.python.org/3/library/stdtypes.html#set).
## Dictionaries in Python

A **dictionary** is an unordered, mutable collection of key-value pairs. Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any type. Dictionaries are widely used for fast lookups and data organization, making them a common interview topic.

### Creating Dictionaries

```python
# Using curly braces
person = {"name": "Alice", "age": 30, "city": "New York"}

# Using dict() constructor
person2 = dict(name="Bob", age=25)

# Empty dictionary
empty_dict = {}
```

### Accessing and Modifying Values

```python
print(person["name"])      # Alice
person["age"] = 31         # Update value
person["email"] = "alice@example.com"  # Add new key-value pair
```

- Accessing a non-existent key raises `KeyError`. Use `.get()` to avoid this:

```python
print(person.get("salary", 0))  # Returns 0 if "salary" not found
```

### Removing Items

- `del person["city"]` — Removes key "city"
- `person.pop("age")` — Removes and returns value for "age"
- `person.clear()` — Removes all items

### Dictionary Methods

| Method                | Description                                      | Example                                 |
|-----------------------|--------------------------------------------------|-----------------------------------------|
| `dict.keys()`         | Returns a view of all keys                       | `person.keys()`                         |
| `dict.values()`       | Returns a view of all values                     | `person.values()`                       |
| `dict.items()`        | Returns a view of (key, value) pairs             | `person.items()`                        |
| `dict.get(key, default)` | Returns value for key or default if not found | `person.get("age", 0)`                  |
| `dict.pop(key[, d])`  | Removes key and returns value (or default)       | `person.pop("age", 0)`                  |
| `dict.update(other)`  | Updates dictionary with key-value pairs from other| `person.update({"country": "USA"})`     |
| `dict.setdefault(key, default)` | Returns value if key exists, else sets it to default | `person.setdefault("salary", 50000)` |
| `dict.copy()`         | Returns a shallow copy of the dictionary         | `copy_person = person.copy()`           |
| `dict.clear()`        | Removes all items                                | `person.clear()`                        |

### Iterating Over Dictionaries

```python
for key in person:
  print(key, person[key])

for key, value in person.items():
  print(f"{key}: {value}")
```

### Dictionary Comprehension

A concise way to create dictionaries:

```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Common Interview Questions and Tips

- **Check if key exists:** Use `in` operator: `'name' in person`
- **Merge dictionaries:** `{**dict1, **dict2}` (Python 3.5+), or `dict1.update(dict2)`
- **Reverse a dictionary:** `reversed_dict = {v: k for k, v in d.items()}`
- **Count frequency:** Use a dictionary or `collections.Counter`
- **Default values:** Use `dict.get()` or `collections.defaultdict`
- **Sorting:** Use `sorted(d.items())` to sort by keys, or `sorted(d.items(), key=lambda x: x[1])` to sort by values

### Example: Counting Character Frequency

```python
s = "banana"
freq = {}
for char in s:
  freq[char] = freq.get(char, 0) + 1
print(freq)  # {'b': 1, 'a': 3, 'n': 2}
```

### Nested Dictionaries

Dictionaries can contain other dictionaries:

```python
students = {
  "Alice": {"age": 20, "grade": "A"},
  "Bob": {"age": 22, "grade": "B"}
}
print(students["Alice"]["grade"])  # A
```

> **Tip:** Dictionaries are unordered before Python 3.7; from 3.7+, insertion order is preserved.

For more, see the [official Python dictionary documentation](https://docs.python.org/3/library/stdtypes.html#dict).


## Object-Oriented Programming (OOP) in Python

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code using objects and classes. It helps structure programs by bundling data and functionality together, making code more modular, reusable, and easier to maintain.

### Classes and Objects

- **Class:** A blueprint for creating objects. It defines attributes (data) and methods (functions) that the objects created from the class will have.
- **Object:** An instance of a class. Each object can have different values for its attributes but shares the structure and behavior defined by the class.

#### Example: Defining and Using a Class

```python
class Dog:
  def __init__(self, name, age):
    self.name = name      # Attribute
    self.age = age        # Attribute

  def bark(self):
    print(f"{self.name} says woof!")

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.bark()  # Output: Buddy says woof!
dog2.bark()  # Output: Max says woof!
```

### The `__init__` Constructor

- The `__init__` method is a special method called a **constructor**.
- It runs automatically when a new object is created from a class.
- It is used to initialize the object's attributes.

```python
class Person:
  def __init__(self, name):
    self.name = name

p = Person("Alice")
print(p.name)  # Output: Alice
```

### The `self` Parameter

- `self` refers to the current instance of the class.
- It is used to access attributes and methods within the class.
- It must be the first parameter of methods in the class (including `__init__`), but you do not pass it explicitly when calling methods.

```python
class Counter:
  def __init__(self):
    self.count = 0

  def increment(self):
    self.count += 1

c = Counter()
c.increment()
print(c.count)  # Output: 1
```

### Key Points

- Use classes to model real-world entities and encapsulate related data and behavior.
- Objects are created from classes and can have unique attribute values.
- The `__init__` constructor initializes new objects.
- Use `self` to refer to the instance inside class methods.

> **Tip:** OOP concepts like inheritance, encapsulation, and polymorphism are also supported in Python for building more complex systems.

For more, see the [official Python OOP documentation](https://docs.python.org/3/tutorial/classes.html).

## Instance vs. Class Attributes

In Python, attributes can be defined at the **instance** level or the **class** level.

### Instance Attributes

- Defined inside methods (usually `__init__`) using `self`.
- Unique to each object (instance) of the class.
- Changing an instance attribute affects only that specific object.

```python
class Car:
  def __init__(self, color):
    self.color = color  # Instance attribute

car1 = Car("red")
car2 = Car("blue")
print(car1.color)  # red
print(car2.color)  # blue
```

### Class Attributes

- Defined directly inside the class, outside any methods.
- Shared by all instances of the class.
- Changing a class attribute affects all instances (unless overridden by an instance attribute).

```python
class Car:
  wheels = 4  # Class attribute

car1 = Car()
car2 = Car()
print(car1.wheels)  # 4
print(car2.wheels)  # 4

Car.wheels = 6
print(car1.wheels)  # 6
print(car2.wheels)  # 6
```

- If you assign to `self.wheels` on an instance, it creates an instance attribute that shadows the class attribute for that object.

> **Tip:** Use class attributes for properties common to all objects, and instance attributes for properties unique to each object.

---

## Object Introspection in Python

**Introspection** is the ability to examine the type or properties of an object at runtime. Python provides several built-in functions and attributes for introspection:

### Common Introspection Tools

- `type(obj)`: Returns the type of the object.
- `id(obj)`: Returns the unique identifier for the object.
- `dir(obj)`: Lists all attributes and methods of the object.
- `hasattr(obj, name)`: Checks if the object has an attribute.
- `getattr(obj, name[, default])`: Gets the value of an attribute.
- `setattr(obj, name, value)`: Sets the value of an attribute.
- `isinstance(obj, cls)`: Checks if the object is an instance of a class or tuple of classes.
- `issubclass(sub, super)`: Checks if a class is a subclass of another.

### Example

```python
class Dog:
  species = "Canine"
  def __init__(self, name):
    self.name = name

d = Dog("Buddy")

print(type(d))            # <class '__main__.Dog'>
print(isinstance(d, Dog)) # True
print(hasattr(d, "name")) # True
print(getattr(d, "name")) # Buddy
print(dir(d))             # Lists all attributes/methods
```

> **Tip:** Introspection is useful for debugging, dynamic programming, and working with unfamiliar objects or libraries.

For more, see the [official Python data model documentation](https://docs.python.org/3/reference/datamodel.html).

## Inheritance and the `super()` Function in Python

**Inheritance** is an OOP feature that allows a class (child or subclass) to inherit attributes and methods from another class (parent or superclass). This promotes code reuse and logical hierarchy.

### Basic Inheritance

To inherit from a class, specify the parent class in parentheses:

```python
class Animal:
  def speak(self):
    print("Animal speaks")

class Dog(Animal):
  def bark(self):
    print("Dog barks")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog
```

### Overriding Methods

A subclass can override methods from its parent class:

```python
class Animal:
  def speak(self):
    print("Animal speaks")

class Cat(Animal):
  def speak(self):
    print("Meow!")

c = Cat()
c.speak()  # Output: Meow!
```

### The `super()` Function

The `super()` function allows you to call methods from the parent class, often used when overriding methods to extend, not replace, parent behavior.

```python
class Animal:
  def __init__(self, name):
    self.name = name

  def speak(self):
    print(f"{self.name} makes a sound")

class Dog(Animal):
  def __init__(self, name, breed):
    super().__init__(name)  # Call parent constructor
    self.breed = breed

  def speak(self):
    super().speak()         # Call parent method
    print(f"{self.name} barks")

d = Dog("Buddy", "Labrador")
d.speak()
# Output:
# Buddy makes a sound
# Buddy barks
```

### Key Points

- Inheritance enables code reuse and logical relationships.
- Use `super()` to access parent class methods and constructors.
- Python supports multiple inheritance, but use it carefully to avoid complexity.

> **Tip:** Use inheritance for "is-a" relationships (e.g., Dog is an Animal).

For more, see the [official Python inheritance documentation](https://docs.python.org/3/tutorial/classes.html#inheritance).

## Method Overriding in Python

**Method overriding** occurs when a subclass provides a specific implementation of a method that is already defined in its parent class. The overridden method in the subclass replaces the parent class’s version when called on an instance of the subclass.

### Example

```python
class Animal:
  def speak(self):
    print("Animal speaks")

class Dog(Animal):
  def speak(self):
    print("Dog barks")

a = Animal()
d = Dog()
a.speak()  # Output: Animal speaks
d.speak()  # Output: Dog barks
```

- The `Dog` class overrides the `speak` method of `Animal`.
- You can still call the parent method using `super()` if needed.

> **Tip:** Overriding is useful for customizing or extending inherited behavior.

---

## Operator Overloading in Python

**Operator overloading** allows you to define custom behavior for standard operators (`+`, `-`, `*`, etc.) in your own classes by implementing special methods (also called "magic methods" or "dunder methods").

### Example: Overloading `+` Operator

```python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Calls p1.__add__(p2)
print(p3.x, p3.y)  # Output: 4 6
```

### Common Operator Overloading Methods

| Operator | Method         | Example Usage   |
|----------|---------------|-----------------|
| `+`      | `__add__`     | `a + b`         |
| `-`      | `__sub__`     | `a - b`         |
| `*`      | `__mul__`     | `a * b`         |
| `/`      | `__truediv__` | `a / b`         |
| `==`     | `__eq__`      | `a == b`        |
| `<`      | `__lt__`      | `a < b`         |

> **Tip:** Operator overloading makes your custom classes behave more like built-in types, improving code readability and usability.

For more, see the [official Python data model documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names).

## Decorators in Python

A **decorator** is a function that takes another function (or method) as input and extends or modifies its behavior without changing its source code. Decorators are widely used for logging, access control, timing, memoization, and more.

### Basic Decorator Syntax

```python
def my_decorator(func):
  def wrapper():
    print("Before function call")
    func()
    print("After function call")
  return wrapper

@my_decorator
def say_hello():
  print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

- The `@my_decorator` syntax is equivalent to `say_hello = my_decorator(say_hello)`.

### Decorators with Arguments

To create a decorator that accepts its own arguments, you need an extra level of nesting: a function that returns a decorator.

```python
def repeat(n):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(n):
        func(*args, **kwargs)
    return wrapper
  return decorator

@repeat(3)
def greet(name):
  print(f"Hello, {name}!")

greet("Alice")
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!
```

- Here, `repeat(3)` returns a decorator that repeats the function call 3 times.

### Key Points

- Decorators are functions that modify the behavior of other functions.
- Use `@decorator_name` syntax for cleaner code.
- Decorators with arguments require an extra enclosing function.
- Use `functools.wraps` to preserve the original function’s metadata (optional but recommended).

> **Tip:** Decorators are a powerful tool for code reuse and separation of concerns.

For more, see the [official Python decorator documentation](https://docs.python.org/3/glossary.html#term-decorator).