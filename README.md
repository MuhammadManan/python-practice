# Python-Practice

Learning Python with CodeWithHarry

## Table of Contents

- [Python Practice Projects 🐍](#python-practice-projects-🐍)
- [Topics Covered](#topics-covered)
- [How to Run](#how-to-run)
- [Note on Python's Typing](#note-on-pythons-typing)
- [Variable Naming Rules in Python](#variable-naming-rules-in-python)
- [Basic Rules of Python](#basic-rules-of-python)
- [Built-in Data Types in Python](#built-in-data-types-in-python)
- [Typecasting in Python](#typecasting-in-python)
- [Operators in Python](#operators-in-python)
  - [Arithmetic Operators](#1-arithmetic-operators)
  - [Assignment Operators](#2-assignment-operators)
  - [Comparison Operators](#3-comparison-operators)
  - [Logical Operators](#4-logical-operators)
  - [Membership Operators](#5-membership-operators)
  - [Identity Operators](#6-identity-operators)
  - [Bitwise Operators](#7-bitwise-operators)
- [Variable Scope and the `global` Keyword in Python](#variable-scope-and-the-global-keyword-in-python)
- [String Methods and Functions in Python](#string-methods-and-functions-in-python)
- [String Formatting: f-Strings and `format()`](#string-formatting-f-strings-and-format)
- [Functions and Arguments in Python](#functions-and-arguments-in-python)
- [Lambda Functions in Python](#lambda-functions-in-python)
- [List Methods in Python](#list-methods-in-python)
- [List Comprehension](#list-comprehension)
- [Tuples in Python](#tuples-in-python)
- [Sets in Python](#sets-in-python)
- [Dictionaries in Python](#dictionaries-in-python)
- [Object-Oriented Programming (OOP) in Python](#object-oriented-programming-oop-in-python)
  - [Instance vs. Class Attributes](#instance-vs-class-attributes)
  - [Object Introspection in Python](#object-introspection-in-python)
  - [Inheritance and the `super()` Function in Python](#inheritance-and-the-super-function-in-python)
  - [Method Overriding in Python](#method-overriding-in-python)
  - [Operator Overloading in Python](#operator-overloading-in-python)
  - [Decorators in Python](#decorators-in-python)
  - [Getters and Setters with Decorators in Python](#getters-and-setters-with-decorators-in-python)
  - [Static Methods and Class Methods in Python](#static-methods-and-class-methods-in-python)
  - [Common Magic (Dunder) Methods in Python](#common-magic-dunder-methods-in-python)
- [Exception Handling and Custom Errors in Python](#exception-handling-and-custom-errors-in-python)
- [`map()`, `filter()`, and `reduce()` in Python](#map-filter-and-reduce-in-python)
- [The Walrus Operator (`:=`) in Python](#the-walrus-operator--in-python)
- [`*args` and `**kwargs` in Python](#args-and-kwargs-in-python)
- [Reading, Writing, and Appending Files in Python](#reading-writing-and-appending-files-in-python)
- [Working with Files and Directories: `os` and `shutil` Modules](#working-with-files-and-directories-os-and-shutil-modules)
- [Virtual Environments and Package Management in Python](#virtual-environments-and-package-management-in-python)
- [The `requests` Module in Python](#the-requests-module-in-python)
- [Regular Expressions (Regex) in Python](#regular-expressions-regex-in-python)
- [Multithreading in Python](#multithreading-in-python)

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

## Variable Scope and the `global` Keyword in Python

**Scope** refers to the region of a program where a variable is recognized. Python uses the LEGB rule to resolve variable names:

- **L**ocal: Names assigned within a function.
- **E**nclosing: Names in the local scope of enclosing functions (nested functions).
- **G**lobal: Names assigned at the top-level of a module or declared global in a function.
- **B**uilt-in: Names preassigned in Python (e.g., `len`, `print`).

### Local vs. Global Variables

- Variables defined inside a function are **local** to that function.
- Variables defined outside any function are **global**.

```python
x = 10  # Global variable

def foo():
  x = 5  # Local variable
  print(x)  # 5

foo()
print(x)  # 10
```

### The `global` Keyword

To modify a global variable inside a function, use the `global` keyword:

```python
count = 0

def increment():
  global count
  count += 1

increment()
print(count)  # 1
```

Without `global`, assigning to `count` inside the function would create a new local variable.

### The `nonlocal` Keyword

For nested functions, use `nonlocal` to modify a variable in the enclosing (non-global) scope:

```python
def outer():
  x = 10
  def inner():
    nonlocal x
    x += 1
  inner()
  print(x)  # 11

outer()
```

### Key Points

- Use local variables for function-specific data.
- Use `global` only when you need to modify a global variable inside a function.
- Prefer passing variables as arguments and returning values for better code clarity.

> **Tip:** Avoid excessive use of `global`—it can make code harder to understand and debug.

For more, see the [official Python documentation on namespaces and scope](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces).


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


## Getters and Setters with Decorators in Python

In Python, **getters** and **setters** are methods used to access and modify the value of private attributes. Instead of calling explicit methods, Python provides the `@property` decorator to define getters, and `@<property>.setter` to define setters, allowing attribute access syntax while still controlling access.

### Why Use Getters and Setters?

- Encapsulate internal data and control how attributes are accessed or modified.
- Add validation, logging, or computed properties without changing the interface.

### Example: Using `@property` and Setter

```python
class Person:
  def __init__(self, name):
    self._name = name  # Convention: _name is "protected"

  @property
  def name(self):
    # Getter method
    return self._name

  @name.setter
  def name(self, value):
    # Setter method with validation
    if not value:
      raise ValueError("Name cannot be empty")
    self._name = value

p = Person("Alice")
print(p.name)      # Calls getter, Output: Alice
p.name = "Bob"     # Calls setter
print(p.name)      # Output: Bob
# p.name = ""      # Raises ValueError
```

- `@property` makes `name` accessible like an attribute, but with getter logic.
- `@name.setter` allows assignment with validation.

### Key Points

- Use `@property` for read-only or computed attributes.
- Use `@<property>.setter` to define how the attribute is set.
- This approach keeps the interface clean and Pythonic.

> **Tip:** Use properties when you need to add logic to attribute access without changing how the attribute is used.

For more, see the [official Python property documentation](https://docs.python.org/3/library/functions.html#property).


## Static Methods and Class Methods in Python

Python supports two special types of methods in classes: **static methods** and **class methods**. Both are defined using decorators and serve different purposes.

### Static Methods

- Defined with the `@staticmethod` decorator.
- Do **not** receive an implicit first argument (`self` or `cls`).
- Behave like regular functions but belong to the class's namespace.
- Used for utility functions related to the class, but not dependent on class or instance data.

**Example:**

```python
class MathUtils:
  @staticmethod
  def add(a, b):
    return a + b

print(MathUtils.add(2, 3))  # Output: 5
```

- You can call static methods on the class or an instance.

### Class Methods

- Defined with the `@classmethod` decorator.
- Receive the class itself as the first argument, conventionally named `cls`.
- Can access and modify class state that applies across all instances.
- Commonly used as alternative constructors or for operations that affect the class as a whole.

**Example:**

```python
class Person:
  count = 0

  def __init__(self, name):
    self.name = name
    Person.count += 1

  @classmethod
  def get_count(cls):
    return cls.count

print(Person.get_count())  # Output: 0
p1 = Person("Alice")
print(Person.get_count())  # Output: 1
```

- Class methods can be called on the class or an instance.

### Key Differences

| Feature         | Static Method         | Class Method           |
|-----------------|----------------------|------------------------|
| Decorator       | `@staticmethod`      | `@classmethod`         |
| First Argument  | None                 | `cls` (the class)      |
| Access to Class | No                   | Yes                    |
| Use Case        | Utility functions    | Alternative constructors, class-wide operations |

> **Tip:** Use static methods for independent utilities, and class methods when you need to access or modify class-level data.

For more, see the [official Python documentation on static and class methods](https://docs.python.org/3/library/functions.html#classmethod).


## Common Magic (Dunder) Methods in Python

**Magic methods** (also called **dunder methods** for "double underscore") are special methods with names like `__init__`, `__str__`, etc. They enable Python's built-in behavior for objects, such as construction, representation, arithmetic, comparison, and more. Understanding these is important for interviews and writing idiomatic Python code.

### Commonly Used Magic Methods

| Method         | Purpose / When Called                        | Example Usage         |
|----------------|----------------------------------------------|----------------------|
| `__init__`     | Object initialization (constructor)          | `obj = MyClass()`    |
| `__str__`      | String representation for `print()`/`str()`  | `print(obj)`         |
| `__repr__`     | Official string representation (debugging)   | `repr(obj)`          |
| `__len__`      | Length of object                             | `len(obj)`           |
| `__getitem__`  | Access item via indexing                     | `obj[key]`           |
| `__setitem__`  | Set item via indexing                        | `obj[key] = value`   |
| `__delitem__`  | Delete item via indexing                     | `del obj[key]`       |
| `__iter__`     | Return iterator for object                   | `for x in obj:`      |
| `__next__`     | Return next item from iterator               | `next(obj)`          |
| `__call__`     | Make object callable like a function         | `obj()`              |
| `__eq__`       | Equality comparison (`==`)                   | `obj1 == obj2`       |
| `__lt__`       | Less than comparison (`<`)                   | `obj1 < obj2`        |
| `__add__`      | Addition operator (`+`)                      | `obj1 + obj2`        |
| `__sub__`      | Subtraction operator (`-`)                   | `obj1 - obj2`        |
| `__mul__`      | Multiplication operator (`*`)                | `obj1 * obj2`        |
| `__contains__` | Membership test (`in`)                       | `item in obj`        |
| `__enter__`    | Context manager entry (`with` statement)     | `with obj:`          |
| `__exit__`     | Context manager exit (`with` statement)      |                      |

### Example: Custom String Representation

```python
class Person:
  def __init__(self, name):
    self.name = name

  def __str__(self):
    return f"Person: {self.name}"

  def __repr__(self):
    return f"Person(name={self.name!r})"

p = Person("Alice")
print(str(p))   # Person: Alice
print(repr(p))  # Person(name='Alice')
```

### Example: Operator Overloading

```python
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2  # Calls __add__
print(p3.x, p3.y)  # 4 6
```

### Example: Making an Object Iterable

```python
class Counter:
  def __init__(self, low, high):
    self.current = low
    self.high = high

  def __iter__(self):
    return self

  def __next__(self):
    if self.current > self.high:
      raise StopIteration
    else:
      self.current += 1
      return self.current - 1

for num in Counter(1, 3):
  print(num)  # 1 2 3
```

> **Tip:** Implementing magic methods lets your objects integrate seamlessly with Python's syntax and built-in functions.

For a full list, see the [official Python data model documentation](https://docs.python.org/3/reference/datamodel.html#special-method-names).

## Exception Handling and Custom Errors in Python

Exception handling is a mechanism that lets you gracefully handle runtime errors, preventing your program from crashing unexpectedly. Python uses `try`, `except`, `else`, and `finally` blocks for this purpose.

### Basic Exception Handling

```python
try:
  # Code that may raise an exception
  x = int(input("Enter a number: "))
  result = 10 / x
except ValueError:
  print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
  print("Cannot divide by zero.")
else:
  print("Result is:", result)
finally:
  print("This block always runs.")
```

- **`try`**: Code that might raise an exception.
- **`except`**: Handle specific exceptions.
- **`else`**: Runs if no exception occurs.
- **`finally`**: Always runs, for cleanup actions.

### Catching Multiple Exceptions

You can handle multiple exceptions in one block:

```python
try:
  # risky code
except (TypeError, ValueError) as e:
  print("Error:", e)
```

### Raising Exceptions

Use `raise` to trigger exceptions intentionally:

```python
def inverse(x):
  if x == 0:
    raise ValueError("Cannot take inverse of zero.")
  return 1 / x
```

### Custom Exceptions

You can define your own exception classes by inheriting from `Exception`:

```python
class NegativeNumberError(Exception):
  """Raised when a negative number is encountered."""
  pass

def sqrt(x):
  if x < 0:
    raise NegativeNumberError("Cannot take square root of a negative number.")
  return x ** 0.5

try:
  sqrt(-4)
except NegativeNumberError as e:
  print("Custom error:", e)
```

### Key Points

- Use exception handling to make your code robust and user-friendly.
- Always catch specific exceptions, not just a bare `except:`.
- Custom exceptions make your error handling clearer and more descriptive.

> **Tip:** Use custom exceptions for application-specific error conditions and to improve code readability.

For more, see the [official Python exceptions documentation](https://docs.python.org/3/tutorial/errors.html).


## `map()`, `filter()`, and `reduce()` in Python

These are powerful built-in functions for functional-style programming, allowing you to process and transform collections efficiently.

### `map()`

- Applies a function to every item in an iterable (like a list) and returns a map object (which can be converted to a list).
- Syntax: `map(function, iterable)`

**Example:**

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]
```

### `filter()`

- Filters items in an iterable based on a function that returns `True` or `False`.
- Only items where the function returns `True` are included.
- Syntax: `filter(function, iterable)`

**Example:**

```python
numbers = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### `reduce()`

- Applies a function cumulatively to the items of an iterable, reducing it to a single value.
- Not a built-in in Python 3; import from `functools`.
- Syntax: `reduce(function, iterable[, initializer])`

**Example:**

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
```

### Key Points

- `map()` transforms each element.
- `filter()` selects elements based on a condition.
- `reduce()` aggregates elements into a single result.
- All three can be replaced by list comprehensions or generator expressions for many use cases, but are concise and expressive for functional programming.

> **Tip:** Use these functions for clean, readable data processing pipelines.

For more, see the [official Python documentation on functional programming tools](https://docs.python.org/3/howto/functional.html).


## The Walrus Operator (`:=`) in Python

The **walrus operator** (`:=`), introduced in Python 3.8, allows you to assign a value to a variable as part of an expression. This can make code more concise and readable, especially in situations where you want to use a value immediately after computing it.

### Basic Syntax

```python
variable := expression
```

### Example: Using the Walrus Operator in a Loop

Without the walrus operator:

```python
line = input("Enter text: ")
while line != "":
  print(f"You entered: {line}")
  line = input("Enter text: ")
```

With the walrus operator:

```python
while (line := input("Enter text: ")) != "":
  print(f"You entered: {line}")
```

### Example: List Comprehension

```python
results = [y for x in range(5) if (y := x * 2) > 5]
print(results)  # [6, 8]
```

### Key Points

- The walrus operator assigns and returns the value in a single expression.
- Useful for reducing code duplication and improving efficiency.
- Can be used in conditions, comprehensions, and anywhere an expression is allowed.

> **Tip:** Use the walrus operator to simplify code, but avoid overusing it in ways that reduce readability.

For more, see the [official Python documentation on assignment expressions](https://docs.python.org/3/whatsnew/3.8.html#assignment-expressions).


## `*args` and `**kwargs` in Python

Python functions can accept a variable number of arguments using `*args` and `**kwargs`. These are especially useful when you don't know in advance how many arguments will be passed to your function.

### `*args` (Non-Keyword Arguments)

- `*args` allows a function to accept any number of positional (non-keyword) arguments.
- Inside the function, `args` is a tuple containing all extra positional arguments.

**Example:**

```python
def add_all(*args):
  return sum(args)

print(add_all(1, 2, 3))        # Output: 6
print(add_all(4, 5, 6, 7, 8))  # Output: 30
```

### `**kwargs` (Keyword Arguments)

- `**kwargs` allows a function to accept any number of keyword arguments (i.e., named arguments).
- Inside the function, `kwargs` is a dictionary containing all extra keyword arguments.

**Example:**

```python
def print_info(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_info(name="Alice", age=30)
# Output:
# name: Alice
# age: 30
```

### Using Both Together

You can use both `*args` and `**kwargs` in the same function. `*args` must come before `**kwargs` in the parameter list.

```python
def demo(a, *args, **kwargs):
  print(a)
  print(args)
  print(kwargs)

demo(1, 2, 3, x=4, y=5)
# Output:
# 1
# (2, 3)
# {'x': 4, 'y': 5}
```

### Key Points

- Use `*args` for variable-length positional arguments.
- Use `**kwargs` for variable-length keyword arguments.
- Useful for function wrappers, decorators, and flexible APIs.

> **Tip:** You can also use `*` and `**` to unpack sequences and dictionaries when calling functions.

For more, see the [official Python documentation on arbitrary argument lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists).


## Reading, Writing, and Appending Files in Python

Python provides built-in functions to work with files, allowing you to read from, write to, and append data to files easily using the `open()` function.

### Opening a File

Use the `open()` function with a file path and mode:

- `'r'` – Read (default)
- `'w'` – Write (creates/truncates file)
- `'a'` – Append (writes at end of file)
- `'b'` – Binary mode (add to mode, e.g., `'rb'`)
- `'+'` – Read and write (e.g., `'r+'`, `'w+'`)

### Reading a File

```python
with open("example.txt", "r") as f:
  content = f.read()
  print(content)
```

- `read()` reads the entire file as a string.
- `readline()` reads one line at a time.
- `readlines()` reads all lines into a list.

### Writing to a File

```python
with open("output.txt", "w") as f:
  f.write("Hello, world!\n")
  f.write("This will overwrite the file.")
```

- `'w'` mode creates the file if it doesn't exist or overwrites it if it does.

### Appending to a File

```python
with open("output.txt", "a") as f:
  f.write("\nThis line is appended.")
```

- `'a'` mode adds content to the end of the file without deleting existing data.

### Example: Reading and Writing

```python
# Read from a file
with open("input.txt", "r") as f:
  data = f.read()

# Write to a new file
with open("copy.txt", "w") as f:
  f.write(data)
```

### Best Practices

- Use `with` statement to automatically close files.
- Always handle exceptions (e.g., with `try`/`except`) for robust code.

> **Tip:** For binary files (images, etc.), use `'rb'` or `'wb'` modes.

For more, see the [official Python file I/O documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).


## Working with Files and Directories: `os` and `shutil` Modules

Python's `os` and `shutil` modules provide powerful tools for interacting with the file system—creating, deleting, moving, and copying files and directories.

### Common `os` Module Functions

- `os.getcwd()`: Get the current working directory.
- `os.chdir(path)`: Change the current working directory.
- `os.listdir(path=".")`: List files and directories in the given path.
- `os.mkdir(path)`: Create a new directory.
- `os.makedirs(path)`: Create directories recursively.
- `os.remove(path)`: Delete a file.
- `os.rmdir(path)`: Remove an empty directory.
- `os.rename(src, dst)`: Rename a file or directory.
- `os.path.exists(path)`: Check if a path exists.
- `os.path.join(a, b, ...)`: Join path components safely.

**Example:**

```python
import os

print(os.getcwd())  # Current directory
os.mkdir("test_dir")  # Create directory
os.chdir("test_dir")  # Change directory
print(os.listdir())  # List contents
os.chdir("..")  # Go back
os.rmdir("test_dir")  # Remove directory
```

### Common `shutil` Module Functions

- `shutil.copy(src, dst)`: Copy a file.
- `shutil.copy2(src, dst)`: Copy a file with metadata.
- `shutil.copytree(src, dst)`: Recursively copy an entire directory tree.
- `shutil.move(src, dst)`: Move a file or directory.
- `shutil.rmtree(path)`: Remove a directory tree (including all files/subdirs).
- `shutil.disk_usage(path)`: Get disk usage statistics.

**Example:**

```python
import shutil

shutil.copy("file.txt", "copy.txt")  # Copy file
shutil.move("copy.txt", "archive/copy.txt")  # Move file
shutil.copytree("src_folder", "dst_folder")  # Copy directory tree
shutil.rmtree("dst_folder")  # Remove directory tree
```

### Tips

- Always use `os.path.join()` for cross-platform path construction.
- Use `with` statements and exception handling for safe file operations.
- Be careful with `shutil.rmtree()` and `os.remove()`—they permanently delete files/directories.

For more, see the [official os documentation](https://docs.python.org/3/library/os.html) and [shutil documentation](https://docs.python.org/3/library/shutil.html).


## Virtual Environments and Package Management in Python

Managing dependencies is crucial for Python projects. **Virtual environments** allow you to isolate project-specific packages, preventing conflicts between projects and keeping your global Python installation clean.

### Why Use Virtual Environments?

- Isolate dependencies for each project.
- Avoid version conflicts between packages.
- Reproduce environments easily for development, testing, and deployment.

### Creating and Activating a Virtual Environment

Use the built-in `venv` module (Python 3.3+):

```bash
python -m venv venv
```

- This creates a `venv` directory with an isolated Python environment.

**Activate the environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

- Your shell prompt will change to indicate the environment is active.

**Deactivate** with:
```bash
deactivate
```

### Installing Packages with `pip`

- Use `pip` to install, upgrade, or remove packages inside the active environment.

```bash
pip install requests
pip uninstall requests
pip list
```

### Managing Dependencies with `requirements.txt`

- Save installed packages:
  ```bash
  pip freeze > requirements.txt
  ```
- Install all dependencies from a file:
  ```bash
  pip install -r requirements.txt
  ```

### Key Points

- Always use a virtual environment for each project.
- Use `pip` for package management.
- Track dependencies with `requirements.txt` for reproducibility.

> **Tip:** Tools like [pipenv](https://pipenv.pypa.io/), [poetry](https://python-poetry.org/), and [conda](https://docs.conda.io/) offer advanced environment and dependency management.

For more, see the [official Python venv documentation](https://docs.python.org/3/library/venv.html) and [pip documentation](https://pip.pypa.io/en/stable/).


## The `requests` Module in Python

The [`requests`](https://docs.python-requests.org/) module is a popular third-party library for making HTTP requests in Python. It provides a simple and user-friendly way to interact with web services and APIs, handling tasks like sending GET/POST requests, handling query parameters, headers, cookies, and more.

### Installing `requests`

Install via pip:

```bash
pip install requests
```

### Basic Usage

**GET request:**

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)      # HTTP status code
print(response.text)             # Response body as string
print(response.json())           # Parse JSON response (if applicable)
```

**POST request:**

```python
payload = {"name": "Alice", "age": 30}
response = requests.post("https://httpbin.org/post", json=payload)
print(response.json())
```

### Common Features

- **Query parameters:**  
  `requests.get(url, params={"key": "value"})`
- **Custom headers:**  
  `requests.get(url, headers={"Authorization": "Bearer TOKEN"})`
- **Timeouts:**  
  `requests.get(url, timeout=5)`
- **Handling errors:**  
  Use `response.raise_for_status()` to raise exceptions for HTTP errors.

### Example: Downloading a File

```python
url = "https://example.com/image.png"
response = requests.get(url)
with open("image.png", "wb") as f:
    f.write(response.content)
```

### Key Points

- `requests` simplifies HTTP requests compared to Python's built-in `urllib`.
- Supports sessions, cookies, authentication, and more.
- Widely used for web scraping, API integration, and automation.

> **Tip:** Always check the response status and handle exceptions for robust code.

For more, see the [official requests documentation](https://docs.python-requests.org/).

## Regular Expressions (Regex) in Python

**Regular expressions** (regex) are patterns used to match, search, and manipulate strings. Python provides the `re` module for working with regular expressions, which is essential for text processing, validation, and data extraction—common in interviews and real-world tasks.

### Basic Usage

Import the `re` module:

```python
import re
```

**Common functions:**

- `re.search(pattern, string)`: Returns a match object if the pattern is found anywhere in the string.
- `re.match(pattern, string)`: Checks for a match only at the beginning of the string.
- `re.findall(pattern, string)`: Returns all non-overlapping matches as a list.
- `re.sub(pattern, repl, string)`: Replaces matches with a replacement string.
- `re.split(pattern, string)`: Splits the string by the occurrences of the pattern.

### Common Patterns and Examples

| Pattern      | Description                  | Example Match      |
|--------------|-----------------------------|--------------------|
| `\d`         | Digit (0-9)                  | `re.findall(r"\d+", "abc123")` → `['123']` |
| `\w`         | Word character (a-z, A-Z, 0-9, _) | `re.findall(r"\w+", "hello_123!")` → `['hello_123']` |
| `\s`         | Whitespace                   | `re.findall(r"\s+", "a b\tc")` → `[' ', '\t']` |
| `.`          | Any character except newline  | `re.findall(r".", "abc")` → `['a', 'b', 'c']` |
| `^` / `$`    | Start / end of string        | `re.match(r"^abc", "abcdef")` |
| `[a-z]`      | Any lowercase letter         | `re.findall(r"[a-z]", "aB1")` → `['a']` |
| `[^0-9]`     | Not a digit                  | `re.findall(r"[^0-9]", "a1b2")` → `['a', 'b']` |
| `a|b`        | a or b                       | `re.findall(r"a|b", "cat bat")` → `['a', 'b', 'a']` |
| `*`, `+`, `?`| 0+ / 1+ / 0 or 1 repetitions | `re.findall(r"ab*", "abbb ac")` → `['abbb', 'a']` |

### Practical Examples

**1. Validate Email Address**

```python
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
email = "test@example.com"
if re.match(pattern, email):
  print("Valid email")
```

**2. Extract All Numbers from a String**

```python
text = "Order 123, shipped on 2023-05-01"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['123', '2023', '05', '01']
```

**3. Replace Multiple Spaces with a Single Space**

```python
s = "This   is   spaced"
clean = re.sub(r"\s+", " ", s)
print(clean)  # "This is spaced"
```

**4. Split a String by Comma or Semicolon**

```python
data = "apple,banana;cherry"
items = re.split(r"[,;]", data)
print(items)  # ['apple', 'banana', 'cherry']
```

### Interview Tips

- Know how to use `re.search`, `re.match`, `re.findall`, and `re.sub`.
- Be familiar with common patterns: digits (`\d`), words (`\w`), whitespace (`\s`), anchors (`^`, `$`), and quantifiers (`*`, `+`, `?`).
- Practice writing regex for validation (emails, phone numbers), extraction (numbers, words), and substitution (removing unwanted characters).

> **Tip:** Use raw strings (`r"pattern"`) to avoid issues with escape sequences.

For more, see the [official Python `re` documentation](https://docs.python.org/3/library/re.html). and wanna dive deeper, go to this link https://regexr.com/

## Multithreading in Python

**Multithreading** allows a program to run multiple threads (smaller units of a process) concurrently, enabling tasks like I/O operations, waiting for user input, or handling multiple network connections to run in parallel. This can improve responsiveness and resource utilization, especially for I/O-bound tasks.

### The `threading` Module

Python's built-in [`threading`](https://docs.python.org/3/library/threading.html) module provides tools for creating and managing threads.

#### Basic Example

```python
import threading

def print_numbers():
  for i in range(5):
    print(f"Number: {i}")

def print_letters():
  for letter in "abcde":
    print(f"Letter: {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()
print("Done!")
```

- `Thread(target=...)` creates a new thread to run a function.
- `.start()` begins thread execution.
- `.join()` waits for the thread to finish.

### When to Use Multithreading

- **I/O-bound tasks:** File operations, network requests, user input, etc.
- **Not for CPU-bound tasks:** Due to Python's Global Interpreter Lock (GIL), threads do not run Python bytecode in true parallel for CPU-heavy work. Use `multiprocessing` for CPU-bound parallelism.

### Thread Synchronization

When threads share data, use synchronization primitives to avoid race conditions:

- `threading.Lock()`: Mutual exclusion lock.
- `threading.Event()`, `threading.Semaphore()`, etc.

**Example with Lock:**

```python
import threading

counter = 0
lock = threading.Lock()

def increment():
  global counter
  for _ in range(1000):
    with lock:
      counter += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)  # 10000
```

### Key Points

- Use threads for I/O-bound concurrency.
- Protect shared data with locks to prevent race conditions.
- For CPU-bound tasks, consider the `multiprocessing` module.

> **Tip:** Threading can make programs more responsive, but always be careful with shared state and synchronization.

For more, see the [official Python threading documentation](https://docs.python.org/3/library/threading.html).


