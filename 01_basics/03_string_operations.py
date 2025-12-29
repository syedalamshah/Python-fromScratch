"""
String Operations in Python

Strings are sequences of characters enclosed in quotes.
"""

# Creating strings
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multi-line string"""

print("=== STRING CREATION ===")
print(f"Single quotes: {single_quote}")
print(f"Double quotes: {double_quote}")
print(f"Triple quotes: {triple_quote}")

# String concatenation
print("\n=== STRING CONCATENATION ===")
greeting = single_quote + " " + double_quote
print(f"Concatenation: {greeting}")

# String repetition
print(f"Repetition: {'Ha' * 3}")

# String indexing and slicing
print("\n=== STRING INDEXING & SLICING ===")
text = "Python Programming"
print(f"Original: {text}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"First 6 characters: {text[0:6]}")
print(f"From index 7 to end: {text[7:]}")
print(f"Last 11 characters: {text[-11:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reverse string: {text[::-1]}")

# String methods
print("\n=== STRING METHODS ===")
sample = "  hello world  "
print(f"Original: '{sample}'")
print(f"Upper: {sample.upper()}")
print(f"Lower: {sample.lower()}")
print(f"Capitalize: {sample.capitalize()}")
print(f"Title: {sample.title()}")
print(f"Strip: '{sample.strip()}'")
print(f"Replace: {sample.replace('world', 'Python')}")

# String formatting
print("\n=== STRING FORMATTING ===")
name = "Alice"
age = 30
# f-strings (Python 3.6+)
print(f"My name is {name} and I am {age} years old.")
# format() method
print("My name is {} and I am {} years old.".format(name, age))
# % formatting (older style)
print("My name is %s and I am %d years old." % (name, age))

# String checking methods
print("\n=== STRING CHECKING METHODS ===")
test_str = "Hello123"
print(f"Is alphanumeric: {test_str.isalnum()}")
print(f"Is alphabetic: {test_str.isalpha()}")
print(f"Is digit: {test_str.isdigit()}")
print(f"Is lowercase: {test_str.islower()}")
print(f"Is uppercase: {test_str.isupper()}")

# String length
print(f"\nLength of '{text}': {len(text)}")

print("\nAll examples executed successfully!")
