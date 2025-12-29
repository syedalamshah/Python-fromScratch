"""
Sets in Python

Sets are unordered collections of unique items.
No duplicate values allowed.
"""

print("=== CREATING SETS ===")
# Empty set (must use set(), {} creates empty dict)
empty_set = set()
print(f"Empty set: {empty_set}, Type: {type(empty_set)}")

# Set with items
fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")

# From list (duplicates removed automatically)
numbers = set([1, 2, 2, 3, 3, 3, 4, 5])
print(f"Numbers (from list with duplicates): {numbers}")

# From string
letters = set("hello")
print(f"Letters from 'hello': {letters}")

print("\n=== SET CHARACTERISTICS ===")
# Unordered - order not guaranteed
test_set = {5, 2, 8, 1, 9}
print(f"Set: {test_set}")

# Unique - duplicates automatically removed
duplicates = {1, 2, 2, 3, 3, 3}
print(f"Duplicates removed: {duplicates}")

# Immutable elements only
# valid_set = {1, 2, [3, 4]}  # Error: list is mutable
valid_set = {1, 2, (3, 4)}  # OK: tuple is immutable
print(f"Set with tuple: {valid_set}")

print("\n=== ADDING ELEMENTS ===")
colors = {"red", "green"}
print(f"Original: {colors}")

# add() - add single element
colors.add("blue")
print(f"After add('blue'): {colors}")

# update() - add multiple elements
colors.update(["yellow", "purple"])
print(f"After update(): {colors}")

# Adding duplicate has no effect
colors.add("red")
print(f"After adding duplicate 'red': {colors}")

print("\n=== REMOVING ELEMENTS ===")
nums = {1, 2, 3, 4, 5}
print(f"Original: {nums}")

# remove() - removes element (raises error if not found)
nums.remove(3)
print(f"After remove(3): {nums}")

# discard() - removes element (no error if not found)
nums.discard(4)
print(f"After discard(4): {nums}")
nums.discard(10)  # No error
print(f"After discard(10) - no error: {nums}")

# pop() - remove and return random element
popped = nums.pop()
print(f"Popped {popped}: {nums}")

# clear() - remove all elements
temp = {1, 2, 3}
temp.clear()
print(f"After clear(): {temp}")

print("\n=== SET OPERATIONS ===")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union - all elements from both sets
print(f"Union (A | B): {set_a | set_b}")
print(f"Union (A.union(B)): {set_a.union(set_b)}")

# Intersection - common elements
print(f"Intersection (A & B): {set_a & set_b}")
print(f"Intersection (A.intersection(B)): {set_a.intersection(set_b)}")

# Difference - elements in A but not in B
print(f"Difference (A - B): {set_a - set_b}")
print(f"Difference (A.difference(B)): {set_a.difference(set_b)}")

# Symmetric Difference - elements in A or B but not both
print(f"Symmetric Diff (A ^ B): {set_a ^ set_b}")
print(f"Symmetric Diff (A.symmetric_difference(B)): {set_a.symmetric_difference(set_b)}")

print("\n=== SET RELATIONSHIPS ===")
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
set3 = {6, 7, 8}

# Subset - all elements of set1 are in set2
print(f"{set1} subset of {set2}: {set1.issubset(set2)}")
print(f"{set1} <= {set2}: {set1 <= set2}")

# Superset - set2 contains all elements of set1
print(f"{set2} superset of {set1}: {set2.issuperset(set1)}")
print(f"{set2} >= {set1}: {set2 >= set1}")

# Disjoint - no common elements
print(f"{set1} disjoint from {set3}: {set1.isdisjoint(set3)}")

print("\n=== SET COMPREHENSION ===")
# Create set from expression
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

print("\n=== CHECKING MEMBERSHIP ===")
fruits = {"apple", "banana", "cherry"}
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")

print("\n=== ITERATING OVER SETS ===")
for fruit in fruits:
    print(f"- {fruit}")

print("\n=== FROZEN SETS ===")
# Immutable version of set
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozen set: {frozen}")
# frozen.add(6)  # Error: frozenset is immutable

# Can be used as dictionary key or set element
nested_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozen sets: {nested_sets}")

print("\n=== PRACTICAL USES ===")
# Remove duplicates from list
numbers_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique_numbers = list(set(numbers_list))
print(f"Original list: {numbers_list}")
print(f"Unique values: {unique_numbers}")

# Find common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"\nCommon elements: {common}")

# Find unique elements in either list
unique_in_either = set(list1) ^ set(list2)
print(f"Unique in either: {unique_in_either}")

print("\n=== SET METHODS SUMMARY ===")
methods = {
    "add()": "Add an element",
    "update()": "Add multiple elements",
    "remove()": "Remove element (error if not found)",
    "discard()": "Remove element (no error)",
    "pop()": "Remove random element",
    "clear()": "Remove all elements",
    "union()": "Combine sets",
    "intersection()": "Common elements",
    "difference()": "Elements in first but not second",
    "symmetric_difference()": "Elements in either but not both"
}
for method, description in methods.items():
    print(f"{method:25} - {description}")

print("\nAll examples executed successfully!")
