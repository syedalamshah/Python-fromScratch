"""
For Loops in Python

For loops are used to iterate over sequences (lists, tuples, strings, etc.)
"""

print("=== BASIC FOR LOOP ===")
# Iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n=== LOOPING THROUGH A STRING ===")
word = "Python"
for letter in word:
    print(letter, end=" ")
print()

print("\n=== USING RANGE() ===")
# range(stop)
print("Range 5:")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop)
print("Range 2 to 6:")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step)
print("Range 0 to 10, step 2:")
for i in range(0, 11, 2):
    print(i, end=" ")
print()

print("\n=== ENUMERATE() ===")
# Get index and value
colors = ["red", "green", "blue"]
for index, color in colors:
    print(f"Index {index}: {color}")

print("\n=== NESTED LOOPS ===")
# Multiplication table
print("3x3 Multiplication Table:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i*j}", end="\t")
    print()

print("\n=== LOOP WITH ELSE ===")
# else block executes if loop completes normally (no break)
for num in range(5):
    print(num, end=" ")
else:
    print("\nLoop completed!")

print("\n=== BREAK STATEMENT ===")
# Exit loop prematurely
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print("\nBroke at 5")

print("\n=== CONTINUE STATEMENT ===")
# Skip current iteration
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("\nOdd numbers only")

print("\n=== PASS STATEMENT ===")
# Placeholder for future code
for i in range(3):
    pass  # Do nothing (placeholder)
print("Pass statement used (no output)")

print("\n=== ITERATING OVER DICTIONARIES ===")
student = {"name": "Alice", "age": 20, "grade": "A"}

print("Keys:")
for key in student.keys():
    print(key, end=" ")
print()

print("Values:")
for value in student.values():
    print(value, end=" ")
print()

print("Key-Value pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n=== LIST COMPREHENSION ===")
# Create a new list using for loop in one line
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# With condition
evens = [n for n in numbers if n % 2 == 0]
print(f"Even numbers: {evens}")

print("\nAll examples executed successfully!")
