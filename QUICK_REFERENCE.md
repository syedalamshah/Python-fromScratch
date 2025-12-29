# Python Quick Reference Guide 📝

A concise cheat sheet for Python fundamentals.

## Basic Syntax

### Variables & Data Types
```python
# Numbers
age = 25                    # int
height = 5.9               # float
name = "Alice"             # str
is_student = True          # bool

# Type conversion
str(42)                    # "42"
int("42")                  # 42
float("3.14")              # 3.14
```

### Operators
```python
# Arithmetic
+  -  *  /  //  %  **      # add, subtract, multiply, divide, floor div, modulo, power

# Comparison
==  !=  >  <  >=  <=       # equal, not equal, greater, less, etc.

# Logical
and  or  not               # logical operators

# Assignment
=  +=  -=  *=  /=          # assign, add to, subtract from, etc.
```

### Strings
```python
# Creation
s = "Hello World"
s = 'Hello World'
s = """Multi
line"""

# Methods
s.upper()                  # "HELLO WORLD"
s.lower()                  # "hello world"
s.strip()                  # remove whitespace
s.split()                  # ["Hello", "World"]
s.replace("H", "J")        # "Jello World"

# Formatting
f"Name: {name}, Age: {age}"
"Name: {}, Age: {}".format(name, age)

# Slicing
s[0]                       # first character
s[-1]                      # last character
s[0:5]                     # first 5 characters
s[::-1]                    # reverse string
```

## Control Flow

### Conditionals
```python
if condition:
    # code
elif another_condition:
    # code
else:
    # code

# Ternary
result = "yes" if condition else "no"
```

### Loops
```python
# For loop
for item in iterable:
    print(item)

for i in range(5):         # 0 to 4
    print(i)

for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)

# While loop
while condition:
    # code

# Loop control
break                      # exit loop
continue                   # skip to next iteration
```

## Data Structures

### Lists (Mutable)
```python
# Create
lst = [1, 2, 3]
lst = []

# Access
lst[0]                     # first item
lst[-1]                    # last item
lst[1:3]                   # slice

# Modify
lst.append(4)              # add to end
lst.insert(0, 0)           # insert at index
lst.remove(2)              # remove first occurrence
lst.pop()                  # remove and return last
lst.clear()                # remove all

# Methods
len(lst)                   # length
sorted(lst)                # return sorted copy
lst.sort()                 # sort in place
lst.reverse()              # reverse in place

# Comprehension
[x**2 for x in range(5)]   # [0, 1, 4, 9, 16]
[x for x in lst if x > 0]  # filter
```

### Tuples (Immutable)
```python
# Create
tup = (1, 2, 3)
tup = 1, 2, 3
tup = (1,)                 # single item

# Unpack
a, b, c = tup
first, *rest = tup
```

### Dictionaries
```python
# Create
d = {"name": "Alice", "age": 30}
d = dict(name="Alice", age=30)

# Access
d["name"]                  # "Alice"
d.get("name")              # "Alice"
d.get("city", "Unknown")   # default value

# Modify
d["city"] = "NYC"          # add/update
del d["age"]               # remove
d.pop("name")              # remove and return

# Methods
d.keys()                   # all keys
d.values()                 # all values
d.items()                  # key-value pairs

# Iteration
for key in d:
    print(key, d[key])

for key, value in d.items():
    print(key, value)

# Comprehension
{k: v**2 for k, v in d.items()}
```

### Sets (Unique Items)
```python
# Create
s = {1, 2, 3}
s = set([1, 2, 2, 3])      # {1, 2, 3}

# Add/Remove
s.add(4)
s.remove(2)
s.discard(5)               # no error if not found

# Operations
s1 | s2                    # union
s1 & s2                    # intersection
s1 - s2                    # difference
s1 ^ s2                    # symmetric difference
```

## Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}"

# Default parameters
def greet(name="World"):
    return f"Hello, {name}"

# Multiple parameters
def add(a, b):
    return a + b

# Variable arguments
def sum_all(*args):
    return sum(args)

# Keyword arguments
def person(**kwargs):
    return kwargs

# Lambda (anonymous)
square = lambda x: x**2
add = lambda a, b: a + b
```

## File Handling

```python
# Write
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Read
with open("file.txt", "r") as f:
    content = f.read()

# Read lines
with open("file.txt", "r") as f:
    lines = f.readlines()

# Append
with open("file.txt", "a") as f:
    f.write("New line\n")

# Modes: 'r' (read), 'w' (write), 'a' (append), 'rb' (binary)
```

## Error Handling

```python
# Try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")

# Try-except-else-finally
try:
    # code
except:
    # handle error
else:
    # runs if no error
finally:
    # always runs

# Raise exception
raise ValueError("Invalid value")
```

## Object-Oriented Programming

```python
# Class
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def bark(self):
        return "Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} ({self.age})"

# Create object
dog = Dog("Buddy", 3)
dog.bark()

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, cuteness):
        super().__init__(name, age)
        self.cuteness = cuteness
    
    def bark(self):
        return "Yip!"
```

## Common Built-in Functions

```python
# Type & Conversion
type(x)                    # get type
int(), float(), str()      # convert types
bool()                     # convert to boolean

# Math
abs(-5)                    # absolute value
round(3.7)                 # round to nearest int
max(1, 2, 3)               # maximum
min(1, 2, 3)               # minimum
sum([1, 2, 3])             # sum of iterable

# Iterables
len(lst)                   # length
sorted(lst)                # sorted copy
reversed(lst)              # reversed iterator
enumerate(lst)             # (index, value) pairs
zip(lst1, lst2)            # combine iterables

# Others
print()                    # output
input()                    # user input
range(5)                   # 0, 1, 2, 3, 4
```

## List Comprehensions

```python
# Basic
[x for x in range(10)]

# With condition
[x for x in range(10) if x % 2 == 0]

# With transformation
[x**2 for x in range(10)]

# Nested
[[i*j for j in range(3)] for i in range(3)]

# Dict comprehension
{x: x**2 for x in range(5)}

# Set comprehension
{x for x in [1, 2, 2, 3]}
```

## Useful Patterns

```python
# Swap variables
a, b = b, a

# Multiple assignment
x, y, z = 1, 2, 3

# Check membership
item in collection

# Iterate with index
for i, item in enumerate(items):
    print(i, item)

# Iterate over multiple lists
for a, b in zip(list1, list2):
    print(a, b)

# Read file lines
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# List from range
list(range(5))             # [0, 1, 2, 3, 4]

# Join strings
"-".join(["a", "b", "c"]) # "a-b-c"

# Split string
"a-b-c".split("-")        # ["a", "b", "c"]
```

## Tips

- Use `help(function)` to get documentation
- Use `dir(object)` to see available methods
- Use f-strings for formatting: `f"Value: {value}"`
- Use list comprehensions for cleaner code
- Always use `with` statement for files
- Use meaningful variable names
- Follow PEP 8 style guide
- Write docstrings for functions
- Handle exceptions appropriately

---

**Note**: This is a quick reference. For detailed explanations, see the example files in each directory!
