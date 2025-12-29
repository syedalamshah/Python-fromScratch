"""
Practice Exercises - Basics

Test your knowledge of Python basics!
Each exercise has a problem description and space for your solution.
"""

print("=" * 60)
print("PYTHON BASICS - PRACTICE EXERCISES")
print("=" * 60)

# Exercise 1: Variables and Data Types
print("\n--- Exercise 1: Variables and Data Types ---")
print("Create variables for:")
print("- Your name (string)")
print("- Your age (integer)")
print("- Your height in meters (float)")
print("- Whether you like Python (boolean)")
print("Then print them all in a formatted message.")

# YOUR SOLUTION HERE:
# name = ?
# age = ?
# height = ?
# likes_python = ?
# print(...)

# Example solution (uncomment to try):
# name = "Student"
# age = 20
# height = 1.75
# likes_python = True
# print(f"My name is {name}, I'm {age} years old, {height}m tall, and I like Python: {likes_python}")

# Exercise 2: Arithmetic Operations
print("\n--- Exercise 2: Arithmetic Operations ---")
print("Write a program that:")
print("- Takes two numbers: 15 and 4")
print("- Calculates and prints: sum, difference, product, division, floor division, modulus")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# a, b = 15, 4
# print(f"Sum: {a + b}")
# print(f"Difference: {a - b}")
# print(f"Product: {a * b}")
# print(f"Division: {a / b}")
# print(f"Floor Division: {a // b}")
# print(f"Modulus: {a % b}")

# Exercise 3: String Manipulation
print("\n--- Exercise 3: String Manipulation ---")
print("Given the string 'Python Programming':")
print("- Print it in uppercase")
print("- Print it in lowercase")
print("- Print only 'Python'")
print("- Print only 'Programming'")
print("- Print the string reversed")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# text = "Python Programming"
# print(f"Uppercase: {text.upper()}")
# print(f"Lowercase: {text.lower()}")
# print(f"First word: {text[:6]}")
# print(f"Second word: {text[7:]}")
# print(f"Reversed: {text[::-1]}")

# Exercise 4: Lists
print("\n--- Exercise 4: Lists ---")
print("Create a list of your 5 favorite fruits:")
print("- Add a new fruit to the end")
print("- Remove the second fruit")
print("- Print the first and last fruits")
print("- Print the length of the list")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# print(f"Original: {fruits}")
# fruits.append("fig")
# print(f"After append: {fruits}")
# fruits.pop(1)
# print(f"After removing second: {fruits}")
# print(f"First: {fruits[0]}, Last: {fruits[-1]}")
# print(f"Length: {len(fruits)}")

# Exercise 5: Conditionals
print("\n--- Exercise 5: Conditionals ---")
print("Write a program that checks a number and prints:")
print("- 'Positive' if number > 0")
print("- 'Negative' if number < 0")
print("- 'Zero' if number == 0")
print("Test with number = -5")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# number = -5
# if number > 0:
#     print("Positive")
# elif number < 0:
#     print("Negative")
# else:
#     print("Zero")

# Exercise 6: Loops
print("\n--- Exercise 6: Loops ---")
print("Print the multiplication table for 7 (7x1 to 7x10)")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# for i in range(1, 11):
#     print(f"7 x {i} = {7 * i}")

# Exercise 7: Functions
print("\n--- Exercise 7: Functions ---")
print("Create a function that:")
print("- Takes two numbers as parameters")
print("- Returns their average")
print("- Test it with 10 and 20")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# def calculate_average(a, b):
#     return (a + b) / 2
#
# result = calculate_average(10, 20)
# print(f"Average of 10 and 20: {result}")

# Exercise 8: Dictionaries
print("\n--- Exercise 8: Dictionaries ---")
print("Create a dictionary with:")
print("- Keys: 'name', 'age', 'city'")
print("- Values: your information")
print("- Print each key-value pair")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# person = {
#     "name": "Alice",
#     "age": 25,
#     "city": "New York"
# }
# for key, value in person.items():
#     print(f"{key}: {value}")

# Exercise 9: List Comprehension
print("\n--- Exercise 9: List Comprehension ---")
print("Create a list of squares of numbers from 1 to 10")
print("Use list comprehension")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# squares = [x**2 for x in range(1, 11)]
# print(f"Squares: {squares}")

# Exercise 10: Challenge - FizzBuzz
print("\n--- Exercise 10: Challenge - FizzBuzz ---")
print("For numbers 1 to 20:")
print("- Print 'Fizz' if divisible by 3")
print("- Print 'Buzz' if divisible by 5")
print("- Print 'FizzBuzz' if divisible by both")
print("- Otherwise print the number")

# YOUR SOLUTION HERE:

# Example solution (uncomment to try):
# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

print("\n" + "=" * 60)
print("TIPS:")
print("- Uncomment the example solutions to see how they work")
print("- Try solving them yourself first!")
print("- Modify the examples to experiment")
print("=" * 60)

print("\nAll exercises loaded successfully!")
print("Uncomment the example solutions to run them.")
