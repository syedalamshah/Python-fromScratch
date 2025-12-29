"""
Operators in Python

Operators are special symbols that perform operations on variables and values.
"""

print("=== ARITHMETIC OPERATORS ===")
a, b = 10, 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("\n=== COMPARISON OPERATORS ===")
x, y = 5, 8

print(f"{x} == {y}: {x == y}")  # Equal to
print(f"{x} != {y}: {x != y}")  # Not equal to
print(f"{x} > {y}: {x > y}")    # Greater than
print(f"{x} < {y}: {x < y}")    # Less than
print(f"{x} >= {y}: {x >= y}")  # Greater than or equal to
print(f"{x} <= {y}: {x <= y}")  # Less than or equal to

print("\n=== LOGICAL OPERATORS ===")
p, q = True, False

print(f"True and False: {p and q}")
print(f"True or False: {p or q}")
print(f"not True: {not p}")

print("\n=== ASSIGNMENT OPERATORS ===")
num = 10
print(f"Initial value: {num}")

num += 5  # Same as num = num + 5
print(f"After += 5: {num}")

num -= 3  # Same as num = num - 3
print(f"After -= 3: {num}")

num *= 2  # Same as num = num * 2
print(f"After *= 2: {num}")

num //= 4  # Same as num = num // 4
print(f"After //= 4: {num}")

print("\n=== IDENTITY OPERATORS ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 is list3: {list1 is list3}")  # True - same object
print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 == list2: {list1 == list2}")  # True - same values

print("\n=== MEMBERSHIP OPERATORS ===")
fruits = ["apple", "banana", "cherry"]

print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'orange' in fruits: {'orange' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

print("\nAll examples executed successfully!")
