"""
Dictionaries in Python

Dictionaries are unordered collections of key-value pairs.
Keys must be unique and immutable (strings, numbers, tuples).
"""

print("=== CREATING DICTIONARIES ===")
# Empty dictionary
empty_dict = {}
print(f"Empty dict: {empty_dict}")

# Dictionary with items
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"Person: {person}")

# Using dict() constructor
student = dict(name="Bob", grade="A", score=95)
print(f"Student: {student}")

# Dictionary with different value types
mixed = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested": {"a": 1, "b": 2}
}
print(f"Mixed types: {mixed}")

print("\n=== ACCESSING VALUES ===")
person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Using get() method (safer - returns None if key doesn't exist)
print(f"City: {person.get('city')}")
print(f"Country: {person.get('country')}")  # Returns None
print(f"Country with default: {person.get('country', 'USA')}")

print("\n=== MODIFYING DICTIONARIES ===")
car = {"brand": "Toyota", "model": "Camry", "year": 2020}
print(f"Original: {car}")

# Update existing value
car["year"] = 2021
print(f"After update: {car}")

# Add new key-value pair
car["color"] = "Blue"
print(f"After adding color: {car}")

# Update multiple items
car.update({"year": 2022, "price": 25000})
print(f"After update(): {car}")

print("\n=== REMOVING ITEMS ===")
fruit_prices = {"apple": 1.5, "banana": 0.5, "cherry": 3.0, "date": 2.0}
print(f"Original: {fruit_prices}")

# pop() - remove and return value
price = fruit_prices.pop("banana")
print(f"Removed banana (${price}): {fruit_prices}")

# popitem() - remove and return last inserted item
item = fruit_prices.popitem()
print(f"Removed last item {item}: {fruit_prices}")

# del - remove specific key
del fruit_prices["cherry"]
print(f"After del: {fruit_prices}")

# clear() - remove all items
temp = {"a": 1, "b": 2}
temp.clear()
print(f"After clear(): {temp}")

print("\n=== DICTIONARY METHODS ===")
data = {"x": 10, "y": 20, "z": 30}
print(f"Dictionary: {data}")

# keys() - get all keys
print(f"Keys: {list(data.keys())}")

# values() - get all values
print(f"Values: {list(data.values())}")

# items() - get all key-value pairs
print(f"Items: {list(data.items())}")

# copy() - create a copy
data_copy = data.copy()
print(f"Copy: {data_copy}")

print("\n=== CHECKING MEMBERSHIP ===")
person = {"name": "Alice", "age": 30}
print(f"'name' in person: {'name' in person}")
print(f"'email' in person: {'email' in person}")
print(f"'Alice' in person.values(): {'Alice' in person.values()}")

print("\n=== ITERATING OVER DICTIONARIES ===")
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

print("Keys:")
for key in scores:
    print(f"  {key}")

print("Values:")
for value in scores.values():
    print(f"  {value}")

print("Key-Value pairs:")
for key, value in scores.items():
    print(f"  {key}: {value}")

print("\n=== NESTED DICTIONARIES ===")
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": [85, 90, 92]
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grades": [78, 85, 88]
    }
}
print(f"Students: {students}")
print(f"Student1 name: {students['student1']['name']}")
print(f"Student2 first grade: {students['student2']['grades'][0]}")

print("\n=== DICTIONARY COMPREHENSION ===")
# Create dictionary from iterable
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From two lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
combined = {k: v for k, v in zip(keys, values)}
print(f"Combined: {combined}")

print("\n=== SETDEFAULT() METHOD ===")
# Get value or set default if key doesn't exist
inventory = {"apples": 10, "bananas": 5}
print(f"Original: {inventory}")

apples = inventory.setdefault("apples", 0)
print(f"Apples: {apples}")

oranges = inventory.setdefault("oranges", 0)
print(f"Oranges: {oranges}, Dictionary: {inventory}")

print("\n=== FROMKEYS() METHOD ===")
# Create dictionary with same value for all keys
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(f"Dictionary with default values: {default_dict}")

print("\n=== MERGING DICTIONARIES ===")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Using update()
merged = dict1.copy()
merged.update(dict2)
print(f"Merged using update(): {merged}")

# Using ** operator (Python 3.5+)
merged2 = {**dict1, **dict2}
print(f"Merged using **: {merged2}")

# Using | operator (Python 3.9+)
merged3 = dict1 | dict2
print(f"Merged using |: {merged3}")

print("\nAll examples executed successfully!")
