"""
Functions in Python

Functions are reusable blocks of code that perform specific tasks.
"""

print("=== BASIC FUNCTION ===")
# Function definition
def greet():
    print("Hello, World!")

# Function call
greet()

print("\n=== FUNCTION WITH PARAMETERS ===")
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

print("\n=== FUNCTION WITH MULTIPLE PARAMETERS ===")
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)
add_numbers(10, 20)

print("\n=== FUNCTION WITH RETURN VALUE ===")
def multiply(x, y):
    return x * y

result = multiply(4, 7)
print(f"4 × 7 = {result}")

print("\n=== FUNCTION WITH DEFAULT PARAMETERS ===")
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")

print("\n=== FUNCTION WITH KEYWORD ARGUMENTS ===")
def describe_person(name, age, city):
    print(f"{name} is {age} years old and lives in {city}")

describe_person(name="Alice", age=30, city="New York")
describe_person(age=25, city="London", name="Bob")

print("\n=== FUNCTION WITH *args (VARIABLE ARGUMENTS) ===")
def sum_all(*numbers):
    total = sum(numbers)
    print(f"Sum of {numbers} = {total}")

sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)

print("\n=== FUNCTION WITH **kwargs (KEYWORD ARGUMENTS) ===")
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print("Person 1:")
print_info(name="Alice", age=30, job="Engineer")
print("Person 2:")
print_info(name="Bob", city="Boston", hobby="Reading")

print("\n=== LAMBDA FUNCTIONS (ANONYMOUS) ===")
# Single line functions
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

add = lambda a, b: a + b
print(f"10 + 15 = {add(10, 15)}")

print("\n=== FUNCTION RETURNING MULTIPLE VALUES ===")
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(nums)
print(f"Numbers: {nums}")
print(f"Min: {minimum}, Max: {maximum}")

print("\n=== NESTED FUNCTIONS ===")
def outer_function(text):
    def inner_function():
        print(f"Inner: {text}")
    
    print("Outer function")
    inner_function()

outer_function("Hello from nested function")

print("\n=== RECURSIVE FUNCTION ===")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"Factorial of 5: {factorial(5)}")

print("\n=== DOCSTRINGS ===")
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width

area = calculate_area(5, 3)
print(f"Area: {area}")
print(f"Docstring: {calculate_area.__doc__}")

print("\nAll examples executed successfully!")
