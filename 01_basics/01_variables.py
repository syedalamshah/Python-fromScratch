"""
Variables and Data Types in Python

Variables are containers for storing data values.
Python is dynamically typed - you don't need to declare variable types.
"""

# Integer - whole numbers
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float - decimal numbers
height = 5.9
print(f"Height: {height}, Type: {type(height)}")

# String - text data
name = "Python Learner"
print(f"Name: {name}, Type: {type(name)}")

# Boolean - True or False
is_learning = True
print(f"Is Learning: {is_learning}, Type: {type(is_learning)}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = 10
print(f"a={a}, b={b}, c={c}")

# Variable naming rules:
# - Must start with letter or underscore
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age, Age, and AGE are different)
# - Cannot use Python keywords (like if, for, while, etc.)

valid_variable_name = "This is valid"
_private_var = "Also valid"
variable123 = "Valid too"

print("\nAll examples executed successfully!")
