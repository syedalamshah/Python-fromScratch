"""
Input and Output in Python

Learn how to get user input and display output.
"""

print("=== BASIC OUTPUT ===")
# print() function is used for output
print("Hello, Python!")
print("Multiple", "arguments", "separated", "by", "commas")
print("Line 1")
print("Line 2")

# Print without newline
print("Same", end=" ")
print("line")

# Print with custom separator
print("A", "B", "C", sep="-")

print("\n=== FORMATTED OUTPUT ===")
# Using f-strings
name = "Python"
version = 3.11
print(f"Language: {name}, Version: {version}")

# Formatting numbers
pi = 3.14159265359
print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Pi rounded to 4 decimals: {pi:.4f}")

number = 1234567
print(f"Formatted number: {number:,}")

print("\n=== INPUT (commented out for automated runs) ===")
# Uncomment these lines to try user input interactively:
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# user_age = input("Enter your age: ")
# user_age = int(user_age)  # Convert string to integer
# print(f"You are {user_age} years old.")

# Example of how input works:
print("# Example: user_name = input('Enter your name: ')")
print("# The input() function always returns a string")
print("# Convert to other types using int(), float(), etc.")

print("\n=== TYPE CONVERSION ===")
# String to integer
str_num = "42"
int_num = int(str_num)
print(f"String '{str_num}' converted to integer: {int_num}")

# String to float
str_float = "3.14"
float_num = float(str_float)
print(f"String '{str_float}' converted to float: {float_num}")

# Integer to string
num = 100
str_version = str(num)
print(f"Integer {num} converted to string: '{str_version}'")

# Other conversions
print(f"Boolean to int: {int(True)}, {int(False)}")
print(f"Integer to boolean: {bool(1)}, {bool(0)}")

print("\nAll examples executed successfully!")
