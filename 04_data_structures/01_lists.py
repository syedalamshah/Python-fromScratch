"""
Lists in Python

Lists are ordered, mutable collections that can contain items of different types.
"""

print("=== CREATING LISTS ===")
# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# List with mixed types
mixed = [1, "hello", 3.14, True]
print(f"Mixed types: {mixed}")

# List with duplicate values
numbers = [1, 2, 2, 3, 3, 3]
print(f"With duplicates: {numbers}")

print("\n=== ACCESSING LIST ELEMENTS ===")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"List: {fruits}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")
print(f"Second to last: {fruits[-2]}")

print("\n=== LIST SLICING ===")
print(f"First 3 items: {fruits[0:3]}")
print(f"From index 2 onward: {fruits[2:]}")
print(f"Last 3 items: {fruits[-3:]}")
print(f"Every 2nd item: {fruits[::2]}")
print(f"Reverse list: {fruits[::-1]}")

print("\n=== MODIFYING LISTS ===")
colors = ["red", "green", "blue"]
print(f"Original: {colors}")

colors[1] = "yellow"
print(f"After modification: {colors}")

colors[0:2] = ["orange", "purple"]
print(f"After slice modification: {colors}")

print("\n=== ADDING ELEMENTS ===")
numbers = [1, 2, 3]
print(f"Original: {numbers}")

# append() - add single item to end
numbers.append(4)
print(f"After append(4): {numbers}")

# insert() - add at specific position
numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")

# extend() - add multiple items
numbers.extend([5, 6, 7])
print(f"After extend([5,6,7]): {numbers}")

print("\n=== REMOVING ELEMENTS ===")
fruits = ["apple", "banana", "cherry", "date", "banana"]
print(f"Original: {fruits}")

# remove() - remove first occurrence
fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

# pop() - remove and return item at index
popped = fruits.pop(2)
print(f"Popped '{popped}': {fruits}")

# pop() without index - removes last item
last = fruits.pop()
print(f"Popped last '{last}': {fruits}")

# del - delete by index or slice
del fruits[0]
print(f"After del fruits[0]: {fruits}")

# clear() - remove all items
temp = [1, 2, 3]
temp.clear()
print(f"After clear(): {temp}")

print("\n=== LIST METHODS ===")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original: {numbers}")

# count() - count occurrences
print(f"Count of 1: {numbers.count(1)}")

# index() - find first occurrence
print(f"Index of 5: {numbers.index(5)}")

# sort() - sort in place
numbers.sort()
print(f"After sort(): {numbers}")

# reverse() - reverse in place
numbers.reverse()
print(f"After reverse(): {numbers}")

# copy() - create a copy
numbers_copy = numbers.copy()
print(f"Copy: {numbers_copy}")

print("\n=== LIST FUNCTIONS ===")
nums = [5, 2, 8, 1, 9]
print(f"List: {nums}")
print(f"Length: {len(nums)}")
print(f"Max: {max(nums)}")
print(f"Min: {min(nums)}")
print(f"Sum: {sum(nums)}")

# sorted() - returns new sorted list (doesn't modify original)
sorted_nums = sorted(nums)
print(f"Sorted (new list): {sorted_nums}")
print(f"Original unchanged: {nums}")

print("\n=== LIST COMPREHENSION ===")
# Create new list from existing list
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers: {evens}")

# With if-else
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print(f"Labels: {labels}")

print("\n=== NESTED LISTS ===")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix: {matrix}")
print(f"Element at [1][2]: {matrix[1][2]}")

print("\n=== CHECKING MEMBERSHIP ===")
fruits = ["apple", "banana", "cherry"]
print(f"'banana' in fruits: {'banana' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")

print("\n=== ITERATING OVER LISTS ===")
for fruit in fruits:
    print(f"- {fruit}")

print("\nWith index:")
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

print("\nAll examples executed successfully!")
