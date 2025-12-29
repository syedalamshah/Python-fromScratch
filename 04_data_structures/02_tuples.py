"""
Tuples in Python

Tuples are ordered, immutable collections.
Similar to lists but cannot be modified after creation.
"""

print("=== CREATING TUPLES ===")
# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with items
fruits = ("apple", "banana", "cherry")
print(f"Fruits: {fruits}")

# Single item tuple (note the comma!)
single = (42,)
print(f"Single item: {single}, Type: {type(single)}")

# Without comma, it's not a tuple
not_tuple = (42)
print(f"Not a tuple: {not_tuple}, Type: {type(not_tuple)}")

# Tuple without parentheses
coordinates = 10, 20, 30
print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")

# Mixed types
mixed = (1, "hello", 3.14, True)
print(f"Mixed types: {mixed}")

print("\n=== ACCESSING TUPLE ELEMENTS ===")
colors = ("red", "green", "blue", "yellow", "purple")
print(f"Tuple: {colors}")
print(f"First item: {colors[0]}")
print(f"Last item: {colors[-1]}")
print(f"Second item: {colors[1]}")

print("\n=== TUPLE SLICING ===")
print(f"First 3: {colors[0:3]}")
print(f"From index 2: {colors[2:]}")
print(f"Last 2: {colors[-2:]}")
print(f"Every 2nd: {colors[::2]}")
print(f"Reverse: {colors[::-1]}")

print("\n=== IMMUTABILITY ===")
numbers = (1, 2, 3, 4, 5)
print(f"Original: {numbers}")
# numbers[0] = 10  # This would raise TypeError: tuples are immutable

# However, you can create a new tuple
new_numbers = (10,) + numbers[1:]
print(f"New tuple: {new_numbers}")

print("\n=== TUPLE METHODS ===")
items = (1, 2, 3, 2, 4, 2, 5)
print(f"Tuple: {items}")

# count() - count occurrences
print(f"Count of 2: {items.count(2)}")

# index() - find first occurrence
print(f"Index of 3: {items.index(3)}")

print("\n=== TUPLE FUNCTIONS ===")
nums = (5, 2, 8, 1, 9, 3)
print(f"Tuple: {nums}")
print(f"Length: {len(nums)}")
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Sum: {sum(nums)}")

print("\n=== TUPLE UNPACKING ===")
# Assign tuple elements to variables
person = ("Alice", 30, "Engineer")
name, age, job = person
print(f"Name: {name}, Age: {age}, Job: {job}")

# Swap variables using tuples
a, b = 5, 10
print(f"Before swap: a={a}, b={b}")
a, b = b, a
print(f"After swap: a={a}, b={b}")

# Unpacking with *
first, *middle, last = (1, 2, 3, 4, 5)
print(f"First: {first}, Middle: {middle}, Last: {last}")

print("\n=== NESTED TUPLES ===")
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
print(f"Matrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

print("\n=== TUPLES WITH MUTABLE ELEMENTS ===")
# Tuple itself is immutable, but can contain mutable objects
tuple_with_list = (1, 2, [3, 4, 5])
print(f"Original: {tuple_with_list}")

# Can modify the list inside
tuple_with_list[2].append(6)
print(f"After modifying list: {tuple_with_list}")

# But can't reassign tuple elements
# tuple_with_list[0] = 10  # This would raise TypeError

print("\n=== CHECKING MEMBERSHIP ===")
fruits = ("apple", "banana", "cherry")
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")

print("\n=== ITERATING OVER TUPLES ===")
for fruit in fruits:
    print(f"- {fruit}")

print("\nWith index:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

print("\n=== WHEN TO USE TUPLES ===")
print("Use tuples when:")
print("1. Data should not change (immutability)")
print("2. Returning multiple values from a function")
print("3. Using as dictionary keys (tuples are hashable)")
print("4. Slightly faster than lists for read-only data")

def get_coordinates():
    return (10, 20)  # Return multiple values as tuple

x, y = get_coordinates()
print(f"\nCoordinates: x={x}, y={y}")

print("\n=== TUPLE AS DICTIONARY KEY ===")
locations = {
    (0, 0): "Origin",
    (1, 0): "East",
    (0, 1): "North"
}
print(f"Locations: {locations}")
print(f"Location at (0,0): {locations[(0, 0)]}")

print("\nAll examples executed successfully!")
